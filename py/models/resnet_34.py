# -*- coding: utf-8 -*-

"""
@date: 2020/4/10 下午9:00
@file: resnet_34.py
@author: zj
@description: 实现残差网络ResNet_34
"""

import torch
from models.res_net import ResNet
from models.basic_block import BasicBlock


def resnet34(num_classes=1000):
    model = ResNet(BasicBlock, [3, 4, 6, 3], num_classes=num_classes)
    return model


if __name__ == '__main__':
    model = resnet34()
    # print(model)

    data = torch.randn((1, 3, 224, 224))
    output = model(data)
    print(output.shape)
