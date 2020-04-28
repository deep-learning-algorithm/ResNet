# -*- coding: utf-8 -*-

"""
@date: 2020/4/28 下午8:31
@file: test_densenet.py
@author: zj
@description: 
"""

import torch
from models.densenet import densenet


def test_densenet121():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = densenet.densenet121(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet169():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = densenet.densenet169(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet201():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = densenet.densenet201(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet264():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = densenet.densenet264(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)
