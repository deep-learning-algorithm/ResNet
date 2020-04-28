# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午2:41
@file: res_net.py
@author: zj
@description: 
"""

import torch
import torch.nn as nn

from models.resnet.basic_block import BasicBlock
from models.resnet.basic_block_v2 import BasicBlock_v2
from models.resnet.bottleneck import Bottleneck
from models.resnet.bottleneck_v2 import Bottleneck_v2
from models.basic_conv2d import BasicConv2d


class ResNet(nn.Module):

    def __init__(self, block, layers, num_classes=1000, zero_init_residual=False, norm_layer=None):
        super(ResNet, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        self._norm_layer = norm_layer

        self.inplanes = 64
        self.conv1 = BasicConv2d(3, self.inplanes, norm_layer=norm_layer,
                                 kernel_size=7, stride=2, padding=3, bias=False)
        # 第一次空间尺寸减半使用Max Pool
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        # 之后固定进行3次空间尺寸衰减：conv3_1、conv4_1、conv5_1
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512 * block.expansion, num_classes)

        # 参数初始化
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        # Zero-initialize the last BN in each residual branch,
        # so that the residual branch starts with zeros, and each residual block behaves like an identity.
        # This improves the model by 0.2~0.3% according to https://arxiv.org/abs/1706.02677
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, Bottleneck):
                    nn.init.constant_(m.bn3.weight, 0)
                elif isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)

    def _make_layer(self, block, planes, blocks, stride=1):
        norm_layer = self._norm_layer
        downsample = None

        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                self.conv1x1(self.inplanes, planes * block.expansion, stride),
                norm_layer(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample, norm_layer))
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.inplanes, planes, norm_layer=norm_layer))

        return nn.Sequential(*layers)

    def _forward_impl(self, x):
        # See note [TorchScript super()]
        x = self.conv1(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def forward(self, x):
        return self._forward_impl(x)

    def conv1x1(self, in_planes, out_planes, stride=1):
        """1x1 convolution"""
        return nn.Conv2d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)


def resnet18(num_classes=1000):
    model = ResNet(BasicBlock, [2, 2, 2, 2], num_classes=num_classes)
    return model


def resnet34(num_classes=1000):
    model = ResNet(BasicBlock, [3, 4, 6, 3], num_classes=num_classes)
    return model


def resnet50(num_classes=1000):
    model = ResNet(Bottleneck, [3, 4, 6, 3], num_classes=num_classes)
    return model


def resnet101(num_classes=1000):
    model = ResNet(Bottleneck, [3, 4, 23, 3], num_classes=num_classes)
    return model


def resnet152(num_classes=1000):
    model = ResNet(Bottleneck, [3, 8, 36, 3], num_classes=num_classes)
    return model


############################ v2

def resnet18_v2(num_classes=1000):
    model = ResNet(BasicBlock_v2, [2, 2, 2, 2], num_classes=num_classes)
    return model


def resnet34_v2(num_classes=1000):
    model = ResNet(BasicBlock_v2, [3, 4, 6, 3], num_classes=num_classes)
    return model


def resnet50_v2(num_classes=1000):
    model = ResNet(Bottleneck_v2, [3, 4, 6, 3], num_classes=num_classes)
    return model


def resnet101_v2(num_classes=1000):
    model = ResNet(Bottleneck_v2, [3, 4, 23, 3], num_classes=num_classes)
    return model


def resnet152_v2(num_classes=1000):
    model = ResNet(Bottleneck_v2, [3, 8, 36, 3], num_classes=num_classes)
    return model
