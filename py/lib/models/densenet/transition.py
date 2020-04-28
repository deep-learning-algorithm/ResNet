# -*- coding: utf-8 -*-

"""
@date: 2020/4/28 下午8:22
@file: transition.py
@author: zj
@description: 
"""

import torch.nn as nn


class Transition(nn.Sequential):
    """
    BN-ReLU-Conv(1x1)-Pool
    执行特征图空间尺寸减半操作
    """

    def __init__(self, num_input_features, num_output_features):
        super(Transition, self).__init__()
        self.add_module('norm', nn.BatchNorm2d(num_input_features))
        self.add_module('relu', nn.ReLU(inplace=True))
        self.add_module('conv', nn.Conv2d(num_input_features, num_output_features,
                                          kernel_size=1, stride=1, bias=False))
        self.add_module('pool', nn.AvgPool2d(kernel_size=2, stride=2))
