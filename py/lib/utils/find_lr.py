# -*- coding: utf-8 -*-

"""
@date: 2020/5/2 下午11:41
@file: find_lr.py
@author: zj
@description: 
"""

import math
import os
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

from utils import util
from models.SmoothLabelCriterion import SmoothLabelCritierion
from models.resnet.res_net import resnet101


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


def find_lr(data_loader, model, criterion, optimizer, device, init_value=1e-8, final_value=10., beta=0.98):
    num = len(data_loader) - 1
    mult = (final_value / init_value) ** (1 / num)
    lr = init_value
    optimizer.param_groups[0]['lr'] = lr
    avg_loss = 0.
    best_loss = 0.
    batch_num = 0
    losses = []
    log_lrs = []
    for inputs, labels in data_loader:
        batch_num += 1
        print('{}: {}'.format(batch_num, lr))

        # As before, get the loss for this mini-batch of inputs/outputs
        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        # Compute the smoothed loss
        avg_loss = beta * avg_loss + (1 - beta) * loss.item()
        smoothed_loss = avg_loss / (1 - beta ** batch_num)

        # Stop if the loss is exploding
        if batch_num > 1 and smoothed_loss > 4 * best_loss:
            return log_lrs, losses

        # Record the best loss
        if smoothed_loss < best_loss or batch_num == 1:
            best_loss = smoothed_loss

        # Store the values
        losses.append(smoothed_loss)
        log_lrs.append(math.log10(lr))

        # Do the SGD step
        loss.backward()
        optimizer.step()

        # Update the lr for the next step
        lr *= mult
        optimizer.param_groups[0]['lr'] = lr
    return log_lrs, losses


if __name__ == '__main__':
    device = util.get_device()
    # device = torch.device('cpu')

    data_loaders, data_sizes = load_data()
    print(data_loaders)
    print(data_sizes)

    res_loss = dict()
    res_top1_acc = dict()
    res_top5_acc = dict()
    num_classes = 100
    num_epochs = 100
    for name in ['resnet']:
        model = resnet101(num_classes=num_classes)
        model.eval()
        # print(model)
        model = model.to(device)

        criterion = SmoothLabelCritierion(label_smoothing=0.1)
        optimizer = optim.Adam(model.parameters(), lr=1e-8)

        print('lr: {}'.format(optimizer.param_groups[0]['lr']))
        log_lrs, losses = find_lr(data_loaders['train'], model, criterion, optimizer, device,
                                  init_value=1e-8, final_value=10., beta=0.98)
        print('lr: {}'.format(optimizer.param_groups[0]['lr']))
        util.plot(log_lrs, losses)
