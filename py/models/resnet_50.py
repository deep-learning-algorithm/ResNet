# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午7:18
@file: resnet_50.py
@author: zj
@description: 
"""

import torch
from models.res_net import ResNet
from models.bottleneck import Bottleneck


def resnet50(num_classes=1000):
    model = ResNet(Bottleneck, [3, 4, 6, 3], num_classes=num_classes)
    return model


if __name__ == '__main__':
    model = resnet50()
    # print(model)

    data = torch.randn((1, 3, 224, 224))
    output = model(data)
    print(output.shape)
