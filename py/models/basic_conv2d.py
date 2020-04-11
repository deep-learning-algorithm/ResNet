# -*- coding: utf-8 -*-

"""
@date: 2020/4/11 下午2:25
@file: basic_conv2d.py
@author: zj
@description: 
"""

import torch.nn as nn
import torch.nn.functional as F


class BasicConv2d(nn.Module):
    """
    结合BN的卷积操作
    """

    def __init__(self, in_channels, out_channels, norm_layer=None, **kwargs):
        super(BasicConv2d, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d

        self.conv = nn.Conv2d(in_channels, out_channels, **kwargs)
        self.bn = norm_layer(out_channels, eps=0.001)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return F.relu(x, inplace=True)
