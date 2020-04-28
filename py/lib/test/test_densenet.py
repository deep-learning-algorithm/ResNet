# -*- coding: utf-8 -*-

"""
@date: 2020/4/28 下午8:31
@file: test_densenet.py
@author: zj
@description: 
"""

import torch
from models.densenet import dense_net


def test_densenet121():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = dense_net.densenet121(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet169():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = dense_net.densenet169(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet201():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = dense_net.densenet201(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_densenet264():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = dense_net.densenet264(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)
