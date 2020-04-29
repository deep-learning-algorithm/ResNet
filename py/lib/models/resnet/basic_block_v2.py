# -*- coding: utf-8 -*-

"""
@date: 2020/4/28 下午9:52
@file: basic_block_v2.py
@author: zj
@description: 
"""

import torch.nn as nn


class BasicBlock_v2(nn.Module):
    """
    两层网络，卷积核大小固定为3x3，每一层的滤波器个数相同
    """

    expansion = 1
    __constants__ = ['downsample']

    def __init__(self, inplanes, planes, stride=1, downsample=None, norm_layer=None):
        super(BasicBlock_v2, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d

        # Both self.conv1 and self.downsample layers downsample the input when stride != 1
        self.bn1 = norm_layer(inplanes)
        self.relu = nn.ReLU(inplace=True)
        self.conv1 = self.conv3x3(inplanes, planes, stride)

        self.conv2 = self.conv3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.bn1(x)
        out = self.relu(out)
        out = self.conv1(out)

        out = self.bn2(out)
        out = self.relu(out)
        out = self.conv2(out)

        if self.downsample is not None:
            # F + x
            identity = self.downsample(x)

        out += identity

        return out

    def conv3x3(self, in_planes, out_planes, stride=1):
        """3x3 convolution with padding"""
        return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1)
