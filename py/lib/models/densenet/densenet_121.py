# -*- coding: utf-8 -*-

"""
@date: 2020/4/27 下午8:22
@file: densenet_121.py
@author: zj
@description: 
"""

import torch
from models.densenet.densenet import DenseNet
from torchvision.models import densenet121


def densenet121(num_classes=1000):
    model = DenseNet(num_classes=num_classes)
    return model


if __name__ == '__main__':
    data = torch.randn((1, 3, 224, 224))
    model = densenet121()
    outputs = model(data)
    print(model)
    print(outputs.shape)
