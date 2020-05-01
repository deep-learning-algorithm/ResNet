# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午2:51
@file: train_resnet.py
@author: zj
@description: 
"""

import time
import copy
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

import warnings

warnings.filterwarnings("ignore")

from utils import util
from utils import metrics
from models.resnet import res_net
from models.SmoothLabelCriterion import SmoothLabelCritierion
from warmup_scheduler import GradualWarmupScheduler


def flops_params():
    for name in ['resnet-50', 'resnet-34', 'resnet-18']:
        if name == 'resnet-50':
            model = res_net.resnet50()
        elif name == 'resnet-34':
            model = res_net.resnet34()
        else:
            model = res_net.resnet18()
        gflops, params_size = metrics.compute_num_flops(model)
        print('{}: {:.3f} GFlops - {:.3f} MB'.format(name, gflops, params_size))


def load_data(data_root_dir):
    train_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        transforms.RandomErasing(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # 测试阶段 Ten Crop test
    test_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.TenCrop(224),
        transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
        transforms.Lambda(lambda crops: torch.stack(
            [transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(crop) for crop in crops]))
    ])

    data_loaders = {}
    data_sizes = {}
    for name in ['train', 'test']:
        data_dir = os.path.join(data_root_dir, name + '_imgs')
        # print(data_dir)

        if name == 'train':
            data_set = ImageFolder(data_dir, transform=train_transform)
            data_loader = DataLoader(data_set, batch_size=96, shuffle=True, num_workers=8)
        else:
            data_set = ImageFolder(data_dir, transform=test_transform)
            data_loader = DataLoader(data_set, batch_size=48, shuffle=True, num_workers=8)
        data_loaders[name] = data_loader
        data_sizes[name] = len(data_set)
    return data_loaders, data_sizes


def train_model(data_loaders, data_sizes, model_name, model, criterion, optimizer, lr_scheduler,
                num_epochs=25, device=None):
    since = time.time()

    best_model_weights = copy.deepcopy(model.state_dict())
    best_top1_acc = 0.0
    best_top5_acc = 0.0

    loss_dict = {'train': [], 'test': []}
    top1_acc_dict = {'train': [], 'test': []}
    top5_acc_dict = {'train': [], 'test': []}
    for epoch in range(num_epochs):

        print('{} - Epoch {}/{}'.format(model_name, epoch + 1, num_epochs))
        print('-' * 10)

        # Each epoch has a training and test phase
        for phase in ['train', 'test']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()  # Set model to evaluate mode

            running_loss = 0.0
            # running_corrects = 0
            running_top1_acc = 0.0
            running_top5_acc = 0.0

            # Iterate over data.
            for inputs, labels in data_loaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    if phase == 'test':
                        N, N_crops, C, H, W = inputs.size()
                        result = model(inputs.view(-1, C, H, W))  # fuse batch size and ncrops
                        outputs = result.view(N, N_crops, -1).mean(1)  # avg over crops
                    else:
                        outputs = model(inputs)
                    # print(outputs.shape)
                    # _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # compute top-k accuray
                    topk_list = metrics.topk_accuracy(outputs, labels, topk=(1, 5))
                    running_top1_acc += topk_list[0]
                    running_top5_acc += topk_list[1]

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                # running_corrects += torch.sum(preds == labels.data)
            if phase == 'train':
                lr_scheduler.step(epoch + 1)
                print('lr: {}'.format(lr_scheduler.get_lr()))

            epoch_loss = running_loss / data_sizes[phase]
            epoch_top1_acc = running_top1_acc / len(data_loaders[phase])
            epoch_top5_acc = running_top5_acc / len(data_loaders[phase])

            loss_dict[phase].append(epoch_loss)
            top1_acc_dict[phase].append(epoch_top1_acc)
            top5_acc_dict[phase].append(epoch_top5_acc)

            print('{} Loss: {:.4f} Top-1 Acc: {:.4f} Top-5 Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_top1_acc, epoch_top5_acc))

            # deep copy the model
            if phase == 'test' and epoch_top1_acc > best_top1_acc:
                best_top1_acc = epoch_top1_acc
                best_model_weights = copy.deepcopy(model.state_dict())
            if phase == 'test' and epoch_top5_acc > best_top5_acc:
                best_top5_acc = epoch_top5_acc

        # 每训练10轮保存一次
        if (epoch + 1) % 10 == 0:
            util.save_model(model.cpu(), '../data/models/%s_%d.pth' % (model_name, epoch + 1))
            model = model.to(device)

    time_elapsed = time.time() - since
    print('Training {} complete in {:.0f}m {:.0f}s'.format(model_name, time_elapsed // 60, time_elapsed % 60))
    print('Best test Top-1 Acc: {:4f}'.format(best_top1_acc))
    print('Best test Top-5 Acc: {:4f}'.format(best_top5_acc))

    # load best model weights
    model.load_state_dict(best_model_weights)
    return model, loss_dict, top1_acc_dict, top5_acc_dict


if __name__ == '__main__':
    flops_params()

    device = util.get_device()
    # device = 'cpu'

    data_loaders, data_sizes = load_data('../data/pascal-voc')
    print(data_loaders)
    print(data_sizes)

    res_loss = dict()
    res_top1_acc = dict()
    res_top5_acc = dict()
    num_classes = 20
    num_epochs = 100
    for name in ['resnet-50', 'resnet-34', 'resnet-18']:
        if name == 'resnet-50':
            model = res_net.resnet50(num_classes=num_classes)
        elif name == 'resnet-34':
            model = res_net.resnet34(num_classes=num_classes)
        else:
            model = res_net.resnet18(num_classes=num_classes)
        model.eval()
        # print(model)
        model = model.to(device)

        criterion = SmoothLabelCritierion(label_smoothing=0.1)
        # criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=2e-3, weight_decay=1e-4)
        # scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.9)
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, num_epochs - 10, eta_min=1e-4)
        lr_scheduler = GradualWarmupScheduler(optimizer, multiplier=1, total_epoch=10, after_scheduler=scheduler)

        util.check_dir('../data/models/')
        best_model, loss_dict, top1_acc_dict, top5_acc_dict = train_model(
            data_loaders, data_sizes, name, model, criterion, optimizer, lr_scheduler,
            num_epochs=num_epochs, device=device)
        # 保存最好的模型参数
        # util.save_model(best_model.cpu(), '../data/models/best_%s.pth' % name)

        res_loss[name] = loss_dict
        res_top1_acc[name] = top1_acc_dict
        res_top5_acc[name] = top5_acc_dict

        print('train %s done' % name)
        print()

    util.save_png('loss', res_loss)
    util.save_png('top-1 acc', res_top1_acc)
    util.save_png('top-5 acc', res_top5_acc)
