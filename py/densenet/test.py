# -*- coding: utf-8 -*-

"""
@date: 2020/4/29 下午10:07
@file: test.py
@author: zj
@description: 
"""

from models.densenet import dense_net
from utils import metrics


def flops_params():
    for name in ['densenet_121', 'densenet_169', 'densenet_201', 'densetNet-264']:
        if name == 'densenet_121':
            model = dense_net.densenet121()
        elif name == 'densenet_169':
            model = dense_net.densenet169()
        elif name == 'densenet_201':
            model = dense_net.densenet201()
        else:
            model = dense_net.densenet264()
        gflops, params_size = metrics.compute_num_flops(model)
        print('{}: {:.3f} GFlops - {:.3f} MB'.format(name, gflops, params_size))


if __name__ == '__main__':
    flops_params()
