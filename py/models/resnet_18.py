# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午2:47
@file: resnet_18.py
@author: zj
@description: 
"""

import torch
from models.res_net import ResNet
from models.basic_block import BasicBlock


def resnet18():
    model = ResNet(BasicBlock, [2, 2, 2, 2])
    return model


if __name__ == '__main__':
    model = resnet18()
    # print(model)

    data = torch.randn((1, 3, 224, 224))
    output = model(data)
    print(output.shape)
