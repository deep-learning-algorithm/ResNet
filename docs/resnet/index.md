# ResNet

`ResNet`通过残差结构的实现，缓解了网络退化的现象，能够用更深的模型（超过`100`层）得到更好的训练结果

##  BasicBlock实现

* 实现文件：`py/lib/models/resnet/basic_block.py`

![](./imgs/figure-2.png)

`ResNet-18/34`使用了`BasicBolck`模块，其实现流程如下：

```
x -> Conv(3x3) -> BN -> ReLU -> Conv(3x3) -> BN -> (+x) -> ReLU
```

## Bottleneck实现

* 实现文件：`py/lib/models/resnet/bottleneck.py`

![](./imgs/figure-5.png)

`ResNet-50/101/152`使用`Bottleneck`模块，通过$1\times 1$卷积来减少特征图个数，其实现流程如下：

```
x -> Conv(1x1) -> BN -> ReLU -> Conv(3x3) -> BN -> ReLU -> Conv(1x1) -> BN -> (+x) -> ReLU
```

## ResNet实现

* 实现文件：`py/lib/models/resnet/resnet.py`

## 训练

比较`ResNet-18、ResNet-34、ResNet-50`

* 数据集：`voc 07+12`
* 损失函数：交叉熵损失
* 优化器：`Adam`，学习率`1e-3`，权重衰减`1e-4`
* 随步长衰减：每隔`7`轮衰减`4%`，学习因子`0.96`
* 迭代次数：`50`

## 训练结果

![](./imgs/loss.png)

![](./imgs/top-1-acc.png)

![](./imgs/top-5-acc.png)

训练日志参考[训练日志](./log-resnet_18-vs-34-vs-50.md)

从结果发现，`ResNet-34`能够比`ResNet-18`得到更好的测试集准确度，不过`ResNet-50`出现了**网络退化现象，说明对于更深网络模型，还需要精心的参数设置和调整**

### 检测精度

* `Top-1 Accuracy`
  * `ResNet-50: 77.60%`
  * `ResNet-34: 81.37%`
  * `ResNet-18: 79.99%`
* `Top-1 Accuracy`
  * `ResNet-50: 97.42%`
  * `ResNet-34: 97.83%`
  * `ResNet-18: 97.48%`

### Flops和参数数目

```
resnet-50: 8.223 GFlops - 97.492 MB
resnet-34: 7.348 GFlops - 83.180 MB
resnet-18: 3.641 GFlops - 44.607 MB
```

## 小结

| CNN Architecture | Data Type (bit) | Model Size (MB) | GFlops （1080Ti） | Top-1 Acc(VOC 07+12) | Top-5 Acc(VOC 07+12) |
|:----------------:|:---------------:|:---------------:|:-----------------:|:--------------------:|:--------------------:|
|     ResNet-18    |        32       |      44.607     |       3.641       |        79.99%        |        97.48%        |
|     ResNet-34    |        32       |      83.180     |       7.348       |        81.37%        |        97.83%        |
|     ResNet-50    |        32       |      97.492     |       8.223       |        77.60%        |        97.42%        |