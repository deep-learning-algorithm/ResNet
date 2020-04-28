# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午7:33
@file: resnet_152.py
@author: zj
@description: 
"""

import torch
from lib.models.resnet.res_net import ResNet
from lib.models.resnet.bottleneck import Bottleneck


def resnet152(num_classes=1000):
    model = ResNet(Bottleneck, [3, 8, 36, 3], num_classes=num_classes)
    return model


if __name__ == '__main__':
    model = resnet152()
    # print(model)

    data = torch.randn((1, 3, 224, 224))
    output = model(data)
    print(output.shape)
