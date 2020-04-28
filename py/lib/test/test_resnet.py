# -*- coding: utf-8 -*-

"""
@date: 2020/4/28 下午9:07
@file: test_resnet.py
@author: zj
@description: 
"""

import torch
from models.resnet import res_net


def test_resnet18():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet18(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet34():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet34(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet50():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet50(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet101():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet101(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet152():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet152(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet18_v2():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet18_v2(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet34_v2():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet34_v2(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet50_v2():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet50_v2(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet101_v2():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet101_v2(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)


def test_resnet152_v2():
    N = 1
    num_classes = 20

    data = torch.randn((N, 3, 224, 224))
    model = res_net.resnet152_v2(num_classes=num_classes)
    outputs = model(data)

    assert outputs.shape == (N, num_classes)
