
# 训练日志

```
$ python train_resnet_v2.py 
resnet-101_v2: 15.668 GFlops - 169.926 MB
resnet-101: 15.668 GFlops - 169.942 MB
{'train': <torch.utils.data.dataloader.DataLoader object at 0x7f6e34ceec50>, 'test': <torch.utils.data.dataloader.DataLoader object at 0x7f6e2e80d190>}
{'train': 40058, 'test': 12032}
resnet-101_v2 - Epoch 1/100
----------
lr: 5.9999999999999995e-05
train Loss: 5.9879 Top-1 Acc: 0.0025 Top-5 Acc: 0.1173
test Loss: 5.9962 Top-1 Acc: 0.0000 Top-5 Acc: 0.1079
resnet-101_v2 - Epoch 2/100
----------
lr: 0.00011999999999999999
train Loss: 1.9051 Top-1 Acc: 39.1542 Top-5 Acc: 75.8261
test Loss: 1.6110 Top-1 Acc: 46.8501 Top-5 Acc: 85.3378
resnet-101_v2 - Epoch 3/100
----------
lr: 0.00017999999999999998
train Loss: 1.6256 Top-1 Acc: 45.8126 Top-5 Acc: 82.8334
test Loss: 1.3562 Top-1 Acc: 54.9054 Top-5 Acc: 88.1267
resnet-101_v2 - Epoch 4/100
----------
lr: 0.00023999999999999998
train Loss: 1.4733 Top-1 Acc: 50.5902 Top-5 Acc: 86.1206
test Loss: 1.2509 Top-1 Acc: 58.4827 Top-5 Acc: 90.3552
resnet-101_v2 - Epoch 5/100
----------
lr: 0.0003
train Loss: 1.3855 Top-1 Acc: 53.1540 Top-5 Acc: 87.8722
test Loss: 1.4576 Top-1 Acc: 51.0458 Top-5 Acc: 86.3173
resnet-101_v2 - Epoch 6/100
----------
/home/lab305/anaconda3/envs/pytorch1.5/lib/python3.7/site-packages/torch/optim/lr_scheduler.py:484: UserWarning: To get the last learning rate computed by the scheduler, please use `get_last_lr()`.
  "please use `get_last_lr()`.", UserWarning)
lr: 0.0003
train Loss: 1.3200 Top-1 Acc: 55.2956 Top-5 Acc: 88.9358
test Loss: 1.1216 Top-1 Acc: 63.4089 Top-5 Acc: 92.2892
resnet-101_v2 - Epoch 7/100
----------
lr: 0.0002999179886011389
train Loss: 1.2407 Top-1 Acc: 58.1479 Top-5 Acc: 90.2656
test Loss: 1.0125 Top-1 Acc: 66.2849 Top-5 Acc: 93.3973
resnet-101_v2 - Epoch 8/100
----------
lr: 0.0002996720440828162
train Loss: 1.1840 Top-1 Acc: 59.6211 Top-5 Acc: 91.3332
test Loss: 1.0035 Top-1 Acc: 65.0149 Top-5 Acc: 93.7376
resnet-101_v2 - Epoch 9/100
----------
lr: 0.0002992624353817517
train Loss: 1.1257 Top-1 Acc: 61.7054 Top-5 Acc: 91.9714
test Loss: 0.8639 Top-1 Acc: 72.9333 Top-5 Acc: 95.3229
resnet-101_v2 - Epoch 10/100
----------
lr: 0.0002986896103990463
train Loss: 1.0895 Top-1 Acc: 62.7921 Top-5 Acc: 92.5806
test Loss: 0.8071 Top-1 Acc: 72.9997 Top-5 Acc: 96.1404
resnet-101_v2 - Epoch 11/100
----------
lr: 0.0002979541955104084
train Loss: 1.0509 Top-1 Acc: 64.0440 Top-5 Acc: 93.1520
test Loss: 0.8018 Top-1 Acc: 73.3607 Top-5 Acc: 96.0284
resnet-101_v2 - Epoch 12/100
----------
lr: 0.00029705699488122143
train Loss: 1.0060 Top-1 Acc: 65.2130 Top-5 Acc: 93.7691
test Loss: 0.7858 Top-1 Acc: 72.5556 Top-5 Acc: 96.1944
resnet-101_v2 - Epoch 13/100
----------
lr: 0.00029599898958720093
train Loss: 0.9795 Top-1 Acc: 66.5536 Top-5 Acc: 94.1757
test Loss: 0.8552 Top-1 Acc: 70.9246 Top-5 Acc: 96.4974
resnet-101_v2 - Epoch 14/100
----------
lr: 0.00029478133654160235
train Loss: 0.9466 Top-1 Acc: 67.6125 Top-5 Acc: 94.4448
test Loss: 1.0320 Top-1 Acc: 64.9527 Top-5 Acc: 93.8621
resnet-101_v2 - Epoch 15/100
----------
lr: 0.0002934053672301537
train Loss: 0.9190 Top-1 Acc: 68.3648 Top-5 Acc: 94.7933
test Loss: 0.7219 Top-1 Acc: 75.4482 Top-5 Acc: 96.4807
resnet-101_v2 - Epoch 16/100
----------
lr: 0.00029187258625509524
train Loss: 0.8990 Top-1 Acc: 69.2987 Top-5 Acc: 94.9833
test Loss: 0.6633 Top-1 Acc: 75.7678 Top-5 Acc: 97.6096
resnet-101_v2 - Epoch 17/100
----------
lr: 0.0002901846696899192
train Loss: 0.8785 Top-1 Acc: 69.6701 Top-5 Acc: 95.2196
test Loss: 0.7261 Top-1 Acc: 75.0332 Top-5 Acc: 96.5139
resnet-101_v2 - Epoch 18/100
----------
lr: 0.0002883434632466078
train Loss: 0.8548 Top-1 Acc: 70.5969 Top-5 Acc: 95.5393
test Loss: 0.6315 Top-1 Acc: 78.0088 Top-5 Acc: 97.5514
resnet-101_v2 - Epoch 19/100
----------
lr: 0.00028635098025737445
train Loss: 0.8301 Top-1 Acc: 71.4868 Top-5 Acc: 95.6990
test Loss: 0.5878 Top-1 Acc: 80.4615 Top-5 Acc: 97.7424
resnet-101_v2 - Epoch 20/100
----------
lr: 0.0002842093994731146
train Loss: 0.8071 Top-1 Acc: 72.1590 Top-5 Acc: 96.0915
test Loss: 0.5906 Top-1 Acc: 80.5653 Top-5 Acc: 97.6344
resnet-101_v2 - Epoch 21/100
----------
lr: 0.0002819210626809734
train Loss: 0.8002 Top-1 Acc: 72.4632 Top-5 Acc: 96.0715
test Loss: 0.5990 Top-1 Acc: 80.2706 Top-5 Acc: 97.7921
resnet-101_v2 - Epoch 22/100
----------
lr: 0.00027948847214363614
train Loss: 0.7768 Top-1 Acc: 73.1489 Top-5 Acc: 96.2924
test Loss: 0.5729 Top-1 Acc: 81.1463 Top-5 Acc: 97.7008
resnet-101_v2 - Epoch 23/100
----------
lr: 0.00027691428786314035
train Loss: 0.7677 Top-1 Acc: 73.6400 Top-5 Acc: 96.5020
test Loss: 0.5461 Top-1 Acc: 81.9223 Top-5 Acc: 98.2445
resnet-101_v2 - Epoch 24/100
----------
lr: 0.00027420132467220304
train Loss: 0.7459 Top-1 Acc: 74.2114 Top-5 Acc: 96.4746
test Loss: 0.5404 Top-1 Acc: 81.2873 Top-5 Acc: 98.1988
resnet-101_v2 - Epoch 25/100
----------
lr: 0.0002713525491562421
train Loss: 0.7292 Top-1 Acc: 75.0290 Top-5 Acc: 96.6892
test Loss: 0.5179 Top-1 Acc: 82.6237 Top-5 Acc: 98.1781
resnet-101_v2 - Epoch 26/100
----------
lr: 0.00026837107640945905
train Loss: 0.7155 Top-1 Acc: 75.3009 Top-5 Acc: 96.9561
test Loss: 0.5053 Top-1 Acc: 82.9390 Top-5 Acc: 98.2653
resnet-101_v2 - Epoch 27/100
----------
lr: 0.00026526016662852886
train Loss: 0.6999 Top-1 Acc: 75.7429 Top-5 Acc: 96.9369
test Loss: 0.4828 Top-1 Acc: 83.8811 Top-5 Acc: 98.5059
resnet-101_v2 - Epoch 28/100
----------
lr: 0.0002620232215476231
train Loss: 0.6922 Top-1 Acc: 76.1350 Top-5 Acc: 97.1382
test Loss: 0.5544 Top-1 Acc: 81.4741 Top-5 Acc: 98.2237
resnet-101_v2 - Epoch 29/100
----------
lr: 0.00025866378071866334
train Loss: 0.6723 Top-1 Acc: 76.9390 Top-5 Acc: 97.2181
test Loss: 0.5315 Top-1 Acc: 82.4867 Top-5 Acc: 98.0370
resnet-101_v2 - Epoch 30/100
----------
lr: 0.00025518551764087326
train Loss: 0.6638 Top-1 Acc: 77.1031 Top-5 Acc: 97.3378
test Loss: 0.4969 Top-1 Acc: 83.6612 Top-5 Acc: 98.2901
resnet-101_v2 - Epoch 31/100
----------
lr: 0.00025159223574386114
train Loss: 0.6504 Top-1 Acc: 77.6186 Top-5 Acc: 97.4401
test Loss: 0.4902 Top-1 Acc: 83.3499 Top-5 Acc: 98.6969
resnet-101_v2 - Epoch 32/100
----------
lr: 0.00024788786422862526
train Loss: 0.6371 Top-1 Acc: 77.9447 Top-5 Acc: 97.5910
test Loss: 0.5108 Top-1 Acc: 81.4990 Top-5 Acc: 98.4644
resnet-101_v2 - Epoch 33/100
----------
lr: 0.00024407645377103052
train Loss: 0.6275 Top-1 Acc: 78.2998 Top-5 Acc: 97.5827
test Loss: 0.4634 Top-1 Acc: 84.5659 Top-5 Acc: 98.5101
resnet-101_v2 - Epoch 34/100
----------
lr: 0.00024016217209245374
train Loss: 0.6122 Top-1 Acc: 79.0584 Top-5 Acc: 97.7820
test Loss: 0.4720 Top-1 Acc: 84.2712 Top-5 Acc: 98.8960
resnet-101_v2 - Epoch 35/100
----------
lr: 0.0002361492994024415
train Loss: 0.5994 Top-1 Acc: 79.2396 Top-5 Acc: 97.8172
test Loss: 0.4424 Top-1 Acc: 85.9354 Top-5 Acc: 98.6304
resnet-101_v2 - Epoch 36/100
----------
lr: 0.00023204222371836405
train Loss: 0.5906 Top-1 Acc: 79.4637 Top-5 Acc: 97.9769
test Loss: 0.4635 Top-1 Acc: 83.9600 Top-5 Acc: 98.7965
resnet-101_v2 - Epoch 37/100
----------
lr: 0.00022784543606718227
train Loss: 0.5810 Top-1 Acc: 79.7864 Top-5 Acc: 97.9715
test Loss: 0.4514 Top-1 Acc: 84.3418 Top-5 Acc: 98.9209
resnet-101_v2 - Epoch 38/100
----------
lr: 0.00022356352557457618
train Loss: 0.5625 Top-1 Acc: 80.8264 Top-5 Acc: 98.0792
test Loss: 0.4328 Top-1 Acc: 85.5868 Top-5 Acc: 98.6139
resnet-101_v2 - Epoch 39/100
----------
lr: 0.00021920117444680317
train Loss: 0.5561 Top-1 Acc: 80.8905 Top-5 Acc: 98.0389
test Loss: 0.4621 Top-1 Acc: 85.1013 Top-5 Acc: 98.6263
resnet-101_v2 - Epoch 40/100
----------
lr: 0.00021476315285077393
train Loss: 0.5396 Top-1 Acc: 81.4523 Top-5 Acc: 98.2414
test Loss: 0.3960 Top-1 Acc: 86.3089 Top-5 Acc: 99.0538
resnet-101_v2 - Epoch 41/100
----------
lr: 0.00021025431369794544
train Loss: 0.5289 Top-1 Acc: 81.9754 Top-5 Acc: 98.2335
test Loss: 0.4312 Top-1 Acc: 85.4042 Top-5 Acc: 98.7882
resnet-101_v2 - Epoch 42/100
----------
lr: 0.0002056795873377331
train Loss: 0.5210 Top-1 Acc: 81.9497 Top-5 Acc: 98.3832
test Loss: 0.4103 Top-1 Acc: 86.5662 Top-5 Acc: 98.9790
resnet-101_v2 - Epoch 43/100
----------
lr: 0.00020104397616624642
train Loss: 0.5084 Top-1 Acc: 82.6819 Top-5 Acc: 98.3508
test Loss: 0.3825 Top-1 Acc: 86.9564 Top-5 Acc: 98.8919
resnet-101_v2 - Epoch 44/100
----------
lr: 0.0001963525491562421
train Loss: 0.4958 Top-1 Acc: 82.9420 Top-5 Acc: 98.6077
test Loss: 0.4164 Top-1 Acc: 85.9479 Top-5 Acc: 98.9127
resnet-101_v2 - Epoch 45/100
----------
lr: 0.00019161043631427672
train Loss: 0.4921 Top-1 Acc: 83.1460 Top-5 Acc: 98.5903
test Loss: 0.4066 Top-1 Acc: 86.1678 Top-5 Acc: 98.8794
resnet-101_v2 - Epoch 46/100
----------
lr: 0.00018682282307111987
train Loss: 0.4815 Top-1 Acc: 83.6097 Top-5 Acc: 98.5832
test Loss: 0.3635 Top-1 Acc: 87.6038 Top-5 Acc: 99.1036
resnet-101_v2 - Epoch 47/100
----------
lr: 0.00018199494461156206
train Loss: 0.4704 Top-1 Acc: 83.8468 Top-5 Acc: 98.6655
test Loss: 0.3773 Top-1 Acc: 87.4004 Top-5 Acc: 99.1783
resnet-101_v2 - Epoch 48/100
----------
lr: 0.00017713208014981646
train Loss: 0.4569 Top-1 Acc: 84.3919 Top-5 Acc: 98.7550
test Loss: 0.3737 Top-1 Acc: 88.0312 Top-5 Acc: 99.1866
resnet-101_v2 - Epoch 49/100
----------
lr: 0.00017223954715677627
train Loss: 0.4459 Top-1 Acc: 84.6825 Top-5 Acc: 98.8223
test Loss: 0.3738 Top-1 Acc: 87.6204 Top-5 Acc: 99.1202
resnet-101_v2 - Epoch 50/100
----------
lr: 0.00016732269554543792
train Loss: 0.4447 Top-1 Acc: 84.9295 Top-5 Acc: 98.8726
test Loss: 0.3886 Top-1 Acc: 86.8153 Top-5 Acc: 99.1866
resnet-101_v2 - Epoch 51/100
----------
lr: 0.00016238690182084984
train Loss: 0.4220 Top-1 Acc: 85.6834 Top-5 Acc: 98.9275
test Loss: 0.3702 Top-1 Acc: 87.4543 Top-5 Acc: 99.0538
resnet-101_v2 - Epoch 52/100
----------
lr: 0.00015743756320098334
train Loss: 0.4209 Top-1 Acc: 85.7978 Top-5 Acc: 98.8377
test Loss: 0.3554 Top-1 Acc: 88.0727 Top-5 Acc: 99.1699
resnet-101_v2 - Epoch 53/100
----------
lr: 0.00015248009171495372
train Loss: 0.4032 Top-1 Acc: 86.2801 Top-5 Acc: 99.0344
test Loss: 0.3496 Top-1 Acc: 88.8986 Top-5 Acc: 99.0870
resnet-101_v2 - Epoch 54/100
----------
lr: 0.0001475199082850462
train Loss: 0.3988 Top-1 Acc: 86.3189 Top-5 Acc: 99.0793
test Loss: 0.3384 Top-1 Acc: 88.7118 Top-5 Acc: 99.1907
resnet-101_v2 - Epoch 55/100
----------
lr: 0.00014256243679901666
train Loss: 0.3883 Top-1 Acc: 87.0029 Top-5 Acc: 99.0872
test Loss: 0.3320 Top-1 Acc: 88.9940 Top-5 Acc: 99.3360
resnet-101_v2 - Epoch 56/100
----------
lr: 0.00013761309817915017
train Loss: 0.3788 Top-1 Acc: 87.1760 Top-5 Acc: 99.1716
test Loss: 0.3594 Top-1 Acc: 88.3300 Top-5 Acc: 99.2115
resnet-101_v2 - Epoch 57/100
----------
lr: 0.0001326773044545621
train Loss: 0.3692 Top-1 Acc: 87.5810 Top-5 Acc: 99.1966
test Loss: 0.3525 Top-1 Acc: 88.3590 Top-5 Acc: 99.1700
resnet-101_v2 - Epoch 58/100
----------
lr: 0.00012776045284322368
train Loss: 0.3615 Top-1 Acc: 87.9977 Top-5 Acc: 99.2290
test Loss: 0.3568 Top-1 Acc: 88.2221 Top-5 Acc: 99.2239
resnet-101_v2 - Epoch 59/100
----------
lr: 0.00012286791985018352
train Loss: 0.3474 Top-1 Acc: 88.3574 Top-5 Acc: 99.2743
test Loss: 0.3402 Top-1 Acc: 88.8571 Top-5 Acc: 99.3111
resnet-101_v2 - Epoch 60/100
----------
lr: 0.00011800505538843798
train Loss: 0.3388 Top-1 Acc: 88.5171 Top-5 Acc: 99.3787
test Loss: 0.3261 Top-1 Acc: 89.1061 Top-5 Acc: 99.2613
resnet-101_v2 - Epoch 61/100
----------
lr: 0.00011317717692888013
train Loss: 0.3250 Top-1 Acc: 89.1483 Top-5 Acc: 99.3862
test Loss: 0.3319 Top-1 Acc: 89.1019 Top-5 Acc: 99.3360
resnet-101_v2 - Epoch 62/100
----------
lr: 0.00010838956368572334
train Loss: 0.3203 Top-1 Acc: 89.4772 Top-5 Acc: 99.3916
test Loss: 0.3183 Top-1 Acc: 89.4381 Top-5 Acc: 99.2571
resnet-101_v2 - Epoch 63/100
----------
lr: 0.00010364745084375793
train Loss: 0.3113 Top-1 Acc: 89.4908 Top-5 Acc: 99.4910
test Loss: 0.3283 Top-1 Acc: 89.4630 Top-5 Acc: 99.1617
resnet-101_v2 - Epoch 64/100
----------
lr: 9.895602383375354e-05
train Loss: 0.3041 Top-1 Acc: 89.8914 Top-5 Acc: 99.4814
test Loss: 0.3394 Top-1 Acc: 88.8571 Top-5 Acc: 99.2737
resnet-101_v2 - Epoch 65/100
----------
lr: 9.43204126622669e-05
train Loss: 0.2950 Top-1 Acc: 90.2752 Top-5 Acc: 99.5110
test Loss: 0.3284 Top-1 Acc: 89.6788 Top-5 Acc: 99.3028
resnet-101_v2 - Epoch 66/100
----------
lr: 8.974568630205462e-05
train Loss: 0.2864 Top-1 Acc: 90.6880 Top-5 Acc: 99.5563
test Loss: 0.3188 Top-1 Acc: 89.8697 Top-5 Acc: 99.3111
resnet-101_v2 - Epoch 67/100
----------
lr: 8.523684714922609e-05
train Loss: 0.2787 Top-1 Acc: 90.9015 Top-5 Acc: 99.5608
test Loss: 0.3178 Top-1 Acc: 89.8490 Top-5 Acc: 99.2530
resnet-101_v2 - Epoch 68/100
----------
lr: 8.079882555319686e-05
train Loss: 0.2659 Top-1 Acc: 91.3007 Top-5 Acc: 99.6182
test Loss: 0.3107 Top-1 Acc: 89.9485 Top-5 Acc: 99.3028
resnet-101_v2 - Epoch 69/100
----------
lr: 7.643647442542379e-05
train Loss: 0.2593 Top-1 Acc: 91.6521 Top-5 Acc: 99.5958
test Loss: 0.3184 Top-1 Acc: 89.7452 Top-5 Acc: 99.3816
resnet-101_v2 - Epoch 70/100
----------
lr: 7.215456393281773e-05
train Loss: 0.2521 Top-1 Acc: 91.9052 Top-5 Acc: 99.6906
test Loss: 0.3177 Top-1 Acc: 89.6207 Top-5 Acc: 99.3774
resnet-101_v2 - Epoch 71/100
----------
lr: 6.795777628163602e-05
train Loss: 0.2463 Top-1 Acc: 92.1287 Top-5 Acc: 99.6707
test Loss: 0.3188 Top-1 Acc: 89.9485 Top-5 Acc: 99.3277
resnet-101_v2 - Epoch 72/100
----------
lr: 6.385070059755848e-05
train Loss: 0.2393 Top-1 Acc: 92.2730 Top-5 Acc: 99.7180
test Loss: 0.3088 Top-1 Acc: 90.2225 Top-5 Acc: 99.3609
resnet-101_v2 - Epoch 73/100
----------
lr: 5.983782790754625e-05
train Loss: 0.2278 Top-1 Acc: 92.7952 Top-5 Acc: 99.7180
test Loss: 0.3050 Top-1 Acc: 90.0025 Top-5 Acc: 99.4605
resnet-101_v2 - Epoch 74/100
----------
lr: 5.592354622896946e-05
train Loss: 0.2222 Top-1 Acc: 92.9919 Top-5 Acc: 99.7206
test Loss: 0.2932 Top-1 Acc: 90.3220 Top-5 Acc: 99.4646
resnet-101_v2 - Epoch 75/100
----------
lr: 5.211213577137471e-05
train Loss: 0.2153 Top-1 Acc: 93.2115 Top-5 Acc: 99.7480
test Loss: 0.2947 Top-1 Acc: 90.4134 Top-5 Acc: 99.3941
resnet-101_v2 - Epoch 76/100
----------
lr: 4.840776425613888e-05
train Loss: 0.2089 Top-1 Acc: 93.3448 Top-5 Acc: 99.7779
test Loss: 0.3204 Top-1 Acc: 89.8531 Top-5 Acc: 99.4024
resnet-101_v2 - Epoch 77/100
----------
lr: 4.481448235912672e-05
train Loss: 0.2069 Top-1 Acc: 93.5404 Top-5 Acc: 99.7804
test Loss: 0.3116 Top-1 Acc: 90.4590 Top-5 Acc: 99.4107
resnet-101_v2 - Epoch 78/100
----------
lr: 4.1336219281336665e-05
train Loss: 0.1967 Top-1 Acc: 93.8776 Top-5 Acc: 99.7804
test Loss: 0.3066 Top-1 Acc: 90.4134 Top-5 Acc: 99.3775
resnet-101_v2 - Epoch 79/100
----------
lr: 3.797677845237697e-05
train Loss: 0.1877 Top-1 Acc: 94.2170 Top-5 Acc: 99.8229
test Loss: 0.3077 Top-1 Acc: 90.4922 Top-5 Acc: 99.4148
resnet-101_v2 - Epoch 80/100
----------
lr: 3.4739833371471137e-05
train Loss: 0.1807 Top-1 Acc: 94.5584 Top-5 Acc: 99.8029
test Loss: 0.3151 Top-1 Acc: 90.0938 Top-5 Acc: 99.3816
resnet-101_v2 - Epoch 81/100
----------
lr: 3.1628923590540984e-05
train Loss: 0.1795 Top-1 Acc: 94.5214 Top-5 Acc: 99.8403
test Loss: 0.3065 Top-1 Acc: 90.6125 Top-5 Acc: 99.4273
resnet-101_v2 - Epoch 82/100
----------
lr: 2.8647450843757904e-05
train Loss: 0.1749 Top-1 Acc: 94.6410 Top-5 Acc: 99.8378
test Loss: 0.3119 Top-1 Acc: 90.3054 Top-5 Acc: 99.3858
resnet-101_v2 - Epoch 83/100
----------
lr: 2.5798675327797e-05
train Loss: 0.1729 Top-1 Acc: 94.7509 Top-5 Acc: 99.8453
test Loss: 0.3068 Top-1 Acc: 90.3054 Top-5 Acc: 99.4190
resnet-101_v2 - Epoch 84/100
----------
lr: 2.308571213685971e-05
train Loss: 0.1653 Top-1 Acc: 95.0632 Top-5 Acc: 99.8453
test Loss: 0.3026 Top-1 Acc: 90.6167 Top-5 Acc: 99.3194
resnet-101_v2 - Epoch 85/100
----------
lr: 2.051152785636392e-05
train Loss: 0.1648 Top-1 Acc: 95.1027 Top-5 Acc: 99.8503
test Loss: 0.3107 Top-1 Acc: 90.4549 Top-5 Acc: 99.3111
resnet-101_v2 - Epoch 86/100
----------
lr: 1.8078937319026657e-05
train Loss: 0.1592 Top-1 Acc: 95.3093 Top-5 Acc: 99.8727
test Loss: 0.3053 Top-1 Acc: 90.7163 Top-5 Acc: 99.4522
resnet-101_v2 - Epoch 87/100
----------
lr: 1.579060052688548e-05
train Loss: 0.1528 Top-1 Acc: 95.4324 Top-5 Acc: 99.8478
test Loss: 0.3072 Top-1 Acc: 90.5295 Top-5 Acc: 99.4439
resnet-101_v2 - Epoch 88/100
----------
lr: 1.3649019742625657e-05
train Loss: 0.1519 Top-1 Acc: 95.5343 Top-5 Acc: 99.8877
test Loss: 0.3125 Top-1 Acc: 90.6208 Top-5 Acc: 99.4065
resnet-101_v2 - Epoch 89/100
----------
lr: 1.1656536753392287e-05
train Loss: 0.1462 Top-1 Acc: 95.8519 Top-5 Acc: 99.8727
test Loss: 0.3047 Top-1 Acc: 90.6623 Top-5 Acc: 99.4605
resnet-101_v2 - Epoch 90/100
----------
lr: 9.815330310080855e-06
train Loss: 0.1450 Top-1 Acc: 95.7614 Top-5 Acc: 99.8902
test Loss: 0.3024 Top-1 Acc: 90.5752 Top-5 Acc: 99.4023
resnet-101_v2 - Epoch 91/100
----------
lr: 8.127413744904804e-06
train Loss: 0.1427 Top-1 Acc: 95.9663 Top-5 Acc: 99.8927
test Loss: 0.3095 Top-1 Acc: 90.8325 Top-5 Acc: 99.4605
resnet-101_v2 - Epoch 92/100
----------
lr: 6.594632769846354e-06
train Loss: 0.1404 Top-1 Acc: 96.0704 Top-5 Acc: 99.8952
test Loss: 0.3115 Top-1 Acc: 90.4382 Top-5 Acc: 99.3774
resnet-101_v2 - Epoch 93/100
----------
lr: 5.218663458397716e-06
train Loss: 0.1416 Top-1 Acc: 95.9585 Top-5 Acc: 99.8827
test Loss: 0.3108 Top-1 Acc: 90.6582 Top-5 Acc: 99.4355
resnet-101_v2 - Epoch 94/100
----------
lr: 4.001010412799139e-06
train Loss: 0.1351 Top-1 Acc: 96.1830 Top-5 Acc: 99.9002
test Loss: 0.3117 Top-1 Acc: 90.4714 Top-5 Acc: 99.4190
resnet-101_v2 - Epoch 95/100
----------
lr: 2.9430051187785967e-06
train Loss: 0.1339 Top-1 Acc: 96.2004 Top-5 Acc: 99.9326
test Loss: 0.3160 Top-1 Acc: 90.3967 Top-5 Acc: 99.4190
resnet-101_v2 - Epoch 96/100
----------
lr: 2.0458044895916517e-06
train Loss: 0.1338 Top-1 Acc: 96.2250 Top-5 Acc: 99.9376
test Loss: 0.3040 Top-1 Acc: 90.8532 Top-5 Acc: 99.4688
resnet-101_v2 - Epoch 97/100
----------
lr: 1.3103896009537207e-06
train Loss: 0.1342 Top-1 Acc: 96.2378 Top-5 Acc: 99.8828
test Loss: 0.3069 Top-1 Acc: 90.5130 Top-5 Acc: 99.4771
resnet-101_v2 - Epoch 98/100
----------
lr: 7.375646182482875e-07
train Loss: 0.1295 Top-1 Acc: 96.4151 Top-5 Acc: 99.9202
test Loss: 0.3115 Top-1 Acc: 90.5005 Top-5 Acc: 99.4771
resnet-101_v2 - Epoch 99/100
----------
lr: 3.2795591718381975e-07
train Loss: 0.1312 Top-1 Acc: 96.3498 Top-5 Acc: 99.8952
test Loss: 0.3185 Top-1 Acc: 90.3428 Top-5 Acc: 99.4356
resnet-101_v2 - Epoch 100/100
----------
lr: 8.201139886109264e-08
train Loss: 0.1317 Top-1 Acc: 96.3149 Top-5 Acc: 99.9177
test Loss: 0.3113 Top-1 Acc: 90.5711 Top-5 Acc: 99.4273
Training resnet-101_v2 complete in 1335m 11s
Best test Top-1 Acc: 90.853233
Best test Top-5 Acc: 99.477089
train resnet-101_v2 done

resnet-101 - Epoch 1/100
----------
lr: 5.9999999999999995e-05
train Loss: 6.4285 Top-1 Acc: 0.0000 Top-5 Acc: 0.0000
test Loss: 6.4217 Top-1 Acc: 0.0000 Top-5 Acc: 0.0000
resnet-101 - Epoch 2/100
----------
lr: 0.00011999999999999999
train Loss: 2.2026 Top-1 Acc: 33.4076 Top-5 Acc: 64.2891
test Loss: 1.9136 Top-1 Acc: 41.7829 Top-5 Acc: 73.3857
resnet-101 - Epoch 3/100
----------
lr: 0.00017999999999999998
train Loss: 1.9432 Top-1 Acc: 37.4581 Top-5 Acc: 72.8313
test Loss: 1.6271 Top-1 Acc: 48.4935 Top-5 Acc: 81.6650
resnet-101 - Epoch 4/100
----------
lr: 0.00023999999999999998
train Loss: 1.7745 Top-1 Acc: 41.8958 Top-5 Acc: 78.1614
test Loss: 1.4640 Top-1 Acc: 53.6687 Top-5 Acc: 86.6409
resnet-101 - Epoch 5/100
----------
lr: 0.0003
train Loss: 1.6470 Top-1 Acc: 45.5723 Top-5 Acc: 81.6661
test Loss: 1.8046 Top-1 Acc: 43.6462 Top-5 Acc: 81.0425
resnet-101 - Epoch 6/100
----------
lr: 0.0003
train Loss: 1.5440 Top-1 Acc: 48.5101 Top-5 Acc: 84.3446
test Loss: 1.5384 Top-1 Acc: 49.2696 Top-5 Acc: 85.3710
resnet-101 - Epoch 7/100
----------
lr: 0.0002999179886011389
train Loss: 1.4514 Top-1 Acc: 51.0496 Top-5 Acc: 86.2512
test Loss: 1.1994 Top-1 Acc: 59.5908 Top-5 Acc: 92.0028
resnet-101 - Epoch 8/100
----------
lr: 0.0002996720440828162
train Loss: 1.3795 Top-1 Acc: 53.2216 Top-5 Acc: 87.6127
test Loss: 1.3046 Top-1 Acc: 60.2424 Top-5 Acc: 91.9613
resnet-101 - Epoch 9/100
----------
lr: 0.0002992624353817517
train Loss: 1.3219 Top-1 Acc: 55.2648 Top-5 Acc: 88.7865
test Loss: 1.1356 Top-1 Acc: 63.2014 Top-5 Acc: 92.5008
resnet-101 - Epoch 10/100
----------
lr: 0.0002986896103990463
train Loss: 1.2667 Top-1 Acc: 56.4596 Top-5 Acc: 89.7617
test Loss: 1.0678 Top-1 Acc: 65.1270 Top-5 Acc: 93.0611
resnet-101 - Epoch 11/100
----------
lr: 0.0002979541955104084
train Loss: 1.2141 Top-1 Acc: 58.5487 Top-5 Acc: 90.6324
test Loss: 0.9923 Top-1 Acc: 65.7495 Top-5 Acc: 94.4887
resnet-101 - Epoch 12/100
----------
lr: 0.00029705699488122143
train Loss: 1.1536 Top-1 Acc: 60.4787 Top-5 Acc: 91.6558
test Loss: 0.9393 Top-1 Acc: 68.2312 Top-5 Acc: 94.9452
resnet-101 - Epoch 13/100
----------
lr: 0.00029599898958720093
train Loss: 1.1174 Top-1 Acc: 61.3370 Top-5 Acc: 92.1087
test Loss: 0.8641 Top-1 Acc: 69.3352 Top-5 Acc: 95.7835
resnet-101 - Epoch 14/100
----------
lr: 0.00029478133654160235
train Loss: 1.0817 Top-1 Acc: 62.6806 Top-5 Acc: 92.5707
test Loss: 0.7925 Top-1 Acc: 72.8254 Top-5 Acc: 96.2732
resnet-101 - Epoch 15/100
----------
lr: 0.0002934053672301537
train Loss: 1.0437 Top-1 Acc: 63.9869 Top-5 Acc: 93.1844
test Loss: 0.8411 Top-1 Acc: 73.7757 Top-5 Acc: 95.8997
resnet-101 - Epoch 16/100
----------
lr: 0.00029187258625509524
train Loss: 1.0063 Top-1 Acc: 65.4063 Top-5 Acc: 93.6980
test Loss: 0.8014 Top-1 Acc: 72.9748 Top-5 Acc: 95.7088
resnet-101 - Epoch 17/100
----------
lr: 0.0002901846696899192
train Loss: 0.9806 Top-1 Acc: 66.0821 Top-5 Acc: 94.0901
test Loss: 0.8348 Top-1 Acc: 71.2733 Top-5 Acc: 96.2691
resnet-101 - Epoch 18/100
----------
lr: 0.0002883434632466078
train Loss: 0.9521 Top-1 Acc: 67.2020 Top-5 Acc: 94.4187
test Loss: 0.7259 Top-1 Acc: 75.3279 Top-5 Acc: 96.9289
resnet-101 - Epoch 19/100
----------
lr: 0.00028635098025737445
train Loss: 0.9149 Top-1 Acc: 68.3011 Top-5 Acc: 94.7305
test Loss: 0.7039 Top-1 Acc: 76.2575 Top-5 Acc: 96.8833
resnet-101 - Epoch 20/100
----------
lr: 0.0002842093994731146
train Loss: 0.8913 Top-1 Acc: 69.1220 Top-5 Acc: 95.1422
test Loss: 0.6358 Top-1 Acc: 79.2040 Top-5 Acc: 97.4933
resnet-101 - Epoch 21/100
----------
lr: 0.0002819210626809734
train Loss: 0.8636 Top-1 Acc: 70.0488 Top-5 Acc: 95.3405
test Loss: 0.6269 Top-1 Acc: 78.0752 Top-5 Acc: 97.6884
resnet-101 - Epoch 22/100
----------
lr: 0.00027948847214363614
train Loss: 0.8466 Top-1 Acc: 70.6660 Top-5 Acc: 95.4798
test Loss: 0.6562 Top-1 Acc: 78.7351 Top-5 Acc: 97.1157
resnet-101 - Epoch 23/100
----------
lr: 0.00027691428786314035
train Loss: 0.8273 Top-1 Acc: 71.2914 Top-5 Acc: 95.6886
test Loss: 0.6294 Top-1 Acc: 79.1874 Top-5 Acc: 97.5722
resnet-101 - Epoch 24/100
----------
lr: 0.00027420132467220304
train Loss: 0.8034 Top-1 Acc: 72.2171 Top-5 Acc: 95.7589
test Loss: 0.6013 Top-1 Acc: 79.3327 Top-5 Acc: 97.6676
resnet-101 - Epoch 25/100
----------
lr: 0.0002713525491562421
train Loss: 0.7855 Top-1 Acc: 72.8984 Top-5 Acc: 96.0483
test Loss: 0.5896 Top-1 Acc: 80.6151 Top-5 Acc: 97.9540
resnet-101 - Epoch 26/100
----------
lr: 0.00026837107640945905
train Loss: 0.7666 Top-1 Acc: 73.5552 Top-5 Acc: 96.2783
test Loss: 0.5535 Top-1 Acc: 80.6565 Top-5 Acc: 97.9706
resnet-101 - Epoch 27/100
----------
lr: 0.00026526016662852886
train Loss: 0.7494 Top-1 Acc: 73.8878 Top-5 Acc: 96.4770
test Loss: 0.5384 Top-1 Acc: 81.6816 Top-5 Acc: 98.1075
resnet-101 - Epoch 28/100
----------
lr: 0.0002620232215476231
train Loss: 0.7357 Top-1 Acc: 74.4027 Top-5 Acc: 96.6571
test Loss: 0.5344 Top-1 Acc: 81.4990 Top-5 Acc: 98.2238
resnet-101 - Epoch 29/100
----------
lr: 0.00025866378071866334
train Loss: 0.7158 Top-1 Acc: 75.2448 Top-5 Acc: 96.8263
test Loss: 0.5301 Top-1 Acc: 82.5282 Top-5 Acc: 97.8959
resnet-101 - Epoch 30/100
----------
lr: 0.00025518551764087326
train Loss: 0.7107 Top-1 Acc: 75.4525 Top-5 Acc: 96.9561
test Loss: 0.4728 Top-1 Acc: 84.6530 Top-5 Acc: 98.4396
resnet-101 - Epoch 31/100
----------
lr: 0.00025159223574386114
train Loss: 0.6878 Top-1 Acc: 76.0220 Top-5 Acc: 97.0884
test Loss: 0.4862 Top-1 Acc: 83.0262 Top-5 Acc: 98.7549
resnet-101 - Epoch 32/100
----------
lr: 0.00024788786422862526
train Loss: 0.6749 Top-1 Acc: 76.4723 Top-5 Acc: 97.1936
test Loss: 0.5256 Top-1 Acc: 82.1298 Top-5 Acc: 98.2984
resnet-101 - Epoch 33/100
----------
lr: 0.00024407645377103052
train Loss: 0.6623 Top-1 Acc: 77.0511 Top-5 Acc: 97.3853
test Loss: 0.4712 Top-1 Acc: 84.0264 Top-5 Acc: 98.7632
resnet-101 - Epoch 34/100
----------
lr: 0.00024016217209245374
train Loss: 0.6538 Top-1 Acc: 77.1410 Top-5 Acc: 97.3802
test Loss: 0.4889 Top-1 Acc: 83.2006 Top-5 Acc: 98.4354
resnet-101 - Epoch 35/100
----------
lr: 0.0002361492994024415
train Loss: 0.6402 Top-1 Acc: 77.6458 Top-5 Acc: 97.4753
test Loss: 0.4639 Top-1 Acc: 84.5825 Top-5 Acc: 98.6886
resnet-101 - Epoch 36/100
----------
lr: 0.00023204222371836405
train Loss: 0.6244 Top-1 Acc: 78.3802 Top-5 Acc: 97.6771
test Loss: 0.4872 Top-1 Acc: 83.7276 Top-5 Acc: 98.4479
resnet-101 - Epoch 37/100
----------
lr: 0.00022784543606718227
train Loss: 0.6133 Top-1 Acc: 78.7270 Top-5 Acc: 97.6430
test Loss: 0.4622 Top-1 Acc: 83.8189 Top-5 Acc: 98.7757
resnet-101 - Epoch 38/100
----------
lr: 0.00022356352557457618
train Loss: 0.6005 Top-1 Acc: 79.1882 Top-5 Acc: 97.8268
test Loss: 0.4807 Top-1 Acc: 83.9558 Top-5 Acc: 98.4727
resnet-101 - Epoch 39/100
----------
lr: 0.00021920117444680317
train Loss: 0.5844 Top-1 Acc: 79.7021 Top-5 Acc: 98.0097
test Loss: 0.4313 Top-1 Acc: 85.1179 Top-5 Acc: 98.7176
resnet-101 - Epoch 40/100
----------
lr: 0.00021476315285077393
train Loss: 0.5755 Top-1 Acc: 79.8288 Top-5 Acc: 98.0738
test Loss: 0.4371 Top-1 Acc: 85.8068 Top-5 Acc: 98.7715
resnet-101 - Epoch 41/100
----------
lr: 0.00021025431369794544
train Loss: 0.5623 Top-1 Acc: 80.4789 Top-5 Acc: 98.1765
test Loss: 0.4191 Top-1 Acc: 85.9230 Top-5 Acc: 98.6886
resnet-101 - Epoch 42/100
----------
lr: 0.0002056795873377331
train Loss: 0.5556 Top-1 Acc: 80.8120 Top-5 Acc: 98.2311
test Loss: 0.4192 Top-1 Acc: 86.0433 Top-5 Acc: 98.8380
resnet-101 - Epoch 43/100
----------
lr: 0.00020104397616624642
train Loss: 0.5405 Top-1 Acc: 81.2777 Top-5 Acc: 98.2210
test Loss: 0.4533 Top-1 Acc: 84.9601 Top-5 Acc: 98.7549
resnet-101 - Epoch 44/100
----------
lr: 0.0001963525491562421
train Loss: 0.5373 Top-1 Acc: 81.4038 Top-5 Acc: 98.2610
test Loss: 0.4072 Top-1 Acc: 85.9603 Top-5 Acc: 99.0537
resnet-101 - Epoch 45/100
----------
lr: 0.00019161043631427672
train Loss: 0.5192 Top-1 Acc: 82.1073 Top-5 Acc: 98.4082
test Loss: 0.3920 Top-1 Acc: 86.7571 Top-5 Acc: 99.0455
resnet-101 - Epoch 46/100
----------
lr: 0.00018682282307111987
train Loss: 0.5085 Top-1 Acc: 82.7431 Top-5 Acc: 98.5030
test Loss: 0.3694 Top-1 Acc: 87.5788 Top-5 Acc: 99.0288
resnet-101 - Epoch 47/100
----------
lr: 0.00018199494461156206
train Loss: 0.4995 Top-1 Acc: 82.6737 Top-5 Acc: 98.5704
test Loss: 0.3843 Top-1 Acc: 87.0726 Top-5 Acc: 98.9957
resnet-101 - Epoch 48/100
----------
lr: 0.00017713208014981646
train Loss: 0.4905 Top-1 Acc: 83.2683 Top-5 Acc: 98.6027
test Loss: 0.3762 Top-1 Acc: 87.7034 Top-5 Acc: 98.8712
resnet-101 - Epoch 49/100
----------
lr: 0.00017223954715677627
train Loss: 0.4756 Top-1 Acc: 83.5207 Top-5 Acc: 98.6501
test Loss: 0.3799 Top-1 Acc: 87.2676 Top-5 Acc: 99.2115
resnet-101 - Epoch 50/100
----------
lr: 0.00016732269554543792
train Loss: 0.4654 Top-1 Acc: 84.1108 Top-5 Acc: 98.7008
test Loss: 0.3904 Top-1 Acc: 86.7157 Top-5 Acc: 98.9624
resnet-101 - Epoch 51/100
----------
lr: 0.00016238690182084984
train Loss: 0.4582 Top-1 Acc: 84.1760 Top-5 Acc: 98.7208
test Loss: 0.3712 Top-1 Acc: 87.9067 Top-5 Acc: 98.9127
resnet-101 - Epoch 52/100
----------
lr: 0.00015743756320098334
train Loss: 0.4407 Top-1 Acc: 84.9262 Top-5 Acc: 98.9549
test Loss: 0.3593 Top-1 Acc: 87.6577 Top-5 Acc: 99.2032
resnet-101 - Epoch 53/100
----------
lr: 0.00015248009171495372
train Loss: 0.4350 Top-1 Acc: 84.9940 Top-5 Acc: 98.9272
test Loss: 0.3634 Top-1 Acc: 87.7656 Top-5 Acc: 99.0911
resnet-101 - Epoch 54/100
----------
lr: 0.0001475199082850462
train Loss: 0.4250 Top-1 Acc: 85.6382 Top-5 Acc: 98.9446
test Loss: 0.3675 Top-1 Acc: 87.7075 Top-5 Acc: 99.0538
resnet-101 - Epoch 55/100
----------
lr: 0.00014256243679901666
train Loss: 0.4134 Top-1 Acc: 85.8107 Top-5 Acc: 99.0244
test Loss: 0.3748 Top-1 Acc: 87.2842 Top-5 Acc: 99.0787
resnet-101 - Epoch 56/100
----------
lr: 0.00013761309817915017
train Loss: 0.4091 Top-1 Acc: 86.0455 Top-5 Acc: 99.1217
test Loss: 0.3434 Top-1 Acc: 88.6828 Top-5 Acc: 99.1866
resnet-101 - Epoch 57/100
----------
lr: 0.0001326773044545621
train Loss: 0.3906 Top-1 Acc: 87.0321 Top-5 Acc: 99.0967
test Loss: 0.3813 Top-1 Acc: 87.3050 Top-5 Acc: 98.8878
resnet-101 - Epoch 58/100
----------
lr: 0.00012776045284322368
train Loss: 0.3881 Top-1 Acc: 86.9152 Top-5 Acc: 99.1791
test Loss: 0.3493 Top-1 Acc: 89.0023 Top-5 Acc: 99.1700
resnet-101 - Epoch 59/100
----------
lr: 0.00012286791985018352
train Loss: 0.3758 Top-1 Acc: 87.3997 Top-5 Acc: 99.2615
test Loss: 0.3612 Top-1 Acc: 87.5788 Top-5 Acc: 99.2031
resnet-101 - Epoch 60/100
----------
lr: 0.00011800505538843798
train Loss: 0.3711 Top-1 Acc: 87.5004 Top-5 Acc: 99.2643
test Loss: 0.3548 Top-1 Acc: 88.2138 Top-5 Acc: 98.9666
resnet-101 - Epoch 61/100
----------
lr: 0.00011317717692888013
train Loss: 0.3641 Top-1 Acc: 87.9723 Top-5 Acc: 99.3513
test Loss: 0.3779 Top-1 Acc: 87.4336 Top-5 Acc: 98.9707
resnet-101 - Epoch 62/100
----------
lr: 0.00010838956368572334
train Loss: 0.3505 Top-1 Acc: 88.3665 Top-5 Acc: 99.3363
test Loss: 0.3512 Top-1 Acc: 88.3923 Top-5 Acc: 99.0662
resnet-101 - Epoch 63/100
----------
lr: 0.00010364745084375793
train Loss: 0.3375 Top-1 Acc: 88.6592 Top-5 Acc: 99.4436
test Loss: 0.3689 Top-1 Acc: 87.5498 Top-5 Acc: 99.0289
resnet-101 - Epoch 64/100
----------
lr: 9.895602383375354e-05
train Loss: 0.3281 Top-1 Acc: 89.0976 Top-5 Acc: 99.4485
test Loss: 0.3376 Top-1 Acc: 89.0604 Top-5 Acc: 99.2779
resnet-101 - Epoch 65/100
----------
lr: 9.43204126622669e-05
train Loss: 0.3190 Top-1 Acc: 89.4993 Top-5 Acc: 99.4885
test Loss: 0.3419 Top-1 Acc: 89.2388 Top-5 Acc: 99.1326
resnet-101 - Epoch 66/100
----------
lr: 8.974568630205462e-05
train Loss: 0.3120 Top-1 Acc: 89.7453 Top-5 Acc: 99.5234
test Loss: 0.3406 Top-1 Acc: 88.9069 Top-5 Acc: 99.1658
resnet-101 - Epoch 67/100
----------
lr: 8.523684714922609e-05
train Loss: 0.2986 Top-1 Acc: 90.2902 Top-5 Acc: 99.5384
test Loss: 0.3359 Top-1 Acc: 89.1932 Top-5 Acc: 99.2862
resnet-101 - Epoch 68/100
----------
lr: 8.079882555319686e-05
train Loss: 0.2899 Top-1 Acc: 90.6915 Top-5 Acc: 99.5634
test Loss: 0.3221 Top-1 Acc: 89.7161 Top-5 Acc: 99.2612
resnet-101 - Epoch 69/100
----------
lr: 7.643647442542379e-05
train Loss: 0.2908 Top-1 Acc: 90.6602 Top-5 Acc: 99.5284
test Loss: 0.3276 Top-1 Acc: 89.4630 Top-5 Acc: 99.2198
resnet-101 - Epoch 70/100
----------
lr: 7.215456393281773e-05
train Loss: 0.2813 Top-1 Acc: 90.9917 Top-5 Acc: 99.6058
test Loss: 0.3341 Top-1 Acc: 89.4464 Top-5 Acc: 99.2986
resnet-101 - Epoch 71/100
----------
lr: 6.795777628163602e-05
train Loss: 0.2766 Top-1 Acc: 91.0965 Top-5 Acc: 99.6307
test Loss: 0.3330 Top-1 Acc: 89.5999 Top-5 Acc: 99.1367
resnet-101 - Epoch 72/100
----------
lr: 6.385070059755848e-05
train Loss: 0.2679 Top-1 Acc: 91.5049 Top-5 Acc: 99.6607
test Loss: 0.3310 Top-1 Acc: 89.4754 Top-5 Acc: 99.2032
resnet-101 - Epoch 73/100
----------
lr: 5.983782790754625e-05
train Loss: 0.2586 Top-1 Acc: 91.9776 Top-5 Acc: 99.6386
test Loss: 0.3266 Top-1 Acc: 89.3675 Top-5 Acc: 99.1949
resnet-101 - Epoch 74/100
----------
lr: 5.592354622896946e-05
train Loss: 0.2467 Top-1 Acc: 92.0739 Top-5 Acc: 99.7205
test Loss: 0.3319 Top-1 Acc: 89.3966 Top-5 Acc: 99.1783
resnet-101 - Epoch 75/100
----------
lr: 5.211213577137471e-05
train Loss: 0.2477 Top-1 Acc: 92.2521 Top-5 Acc: 99.7530
test Loss: 0.3248 Top-1 Acc: 89.7784 Top-5 Acc: 99.1949
resnet-101 - Epoch 76/100
----------
lr: 4.840776425613888e-05
train Loss: 0.2343 Top-1 Acc: 92.8326 Top-5 Acc: 99.7334
test Loss: 0.3299 Top-1 Acc: 89.9485 Top-5 Acc: 99.2903
resnet-101 - Epoch 77/100
----------
lr: 4.481448235912672e-05
train Loss: 0.2323 Top-1 Acc: 92.7271 Top-5 Acc: 99.7355
test Loss: 0.3178 Top-1 Acc: 90.1602 Top-5 Acc: 99.2530
resnet-101 - Epoch 78/100
----------
lr: 4.1336219281336665e-05
train Loss: 0.2303 Top-1 Acc: 93.0750 Top-5 Acc: 99.7230
test Loss: 0.3324 Top-1 Acc: 89.7079 Top-5 Acc: 99.1451
resnet-101 - Epoch 79/100
----------
lr: 3.797677845237697e-05
train Loss: 0.2230 Top-1 Acc: 93.3113 Top-5 Acc: 99.7380
test Loss: 0.3268 Top-1 Acc: 90.0398 Top-5 Acc: 99.2613
resnet-101 - Epoch 80/100
----------
lr: 3.4739833371471137e-05
train Loss: 0.2139 Top-1 Acc: 93.5130 Top-5 Acc: 99.7954
test Loss: 0.3233 Top-1 Acc: 89.9776 Top-5 Acc: 99.2198
resnet-101 - Epoch 81/100
----------
lr: 3.1628923590540984e-05
train Loss: 0.2076 Top-1 Acc: 93.6039 Top-5 Acc: 99.8029
test Loss: 0.3216 Top-1 Acc: 89.9942 Top-5 Acc: 99.2281
resnet-101 - Epoch 82/100
----------
lr: 2.8647450843757904e-05
train Loss: 0.2068 Top-1 Acc: 93.7715 Top-5 Acc: 99.7679
test Loss: 0.3197 Top-1 Acc: 90.1270 Top-5 Acc: 99.2820
resnet-101 - Epoch 83/100
----------
lr: 2.5798675327797e-05
train Loss: 0.1986 Top-1 Acc: 94.1604 Top-5 Acc: 99.7929
test Loss: 0.3216 Top-1 Acc: 90.0025 Top-5 Acc: 99.3111
resnet-101 - Epoch 84/100
----------
lr: 2.308571213685971e-05
train Loss: 0.1967 Top-1 Acc: 94.1700 Top-5 Acc: 99.8378
test Loss: 0.3151 Top-1 Acc: 90.1809 Top-5 Acc: 99.2654
resnet-101 - Epoch 85/100
----------
lr: 2.051152785636392e-05
train Loss: 0.1888 Top-1 Acc: 94.4715 Top-5 Acc: 99.8378
test Loss: 0.3147 Top-1 Acc: 90.3511 Top-5 Acc: 99.2114
resnet-101 - Epoch 86/100
----------
lr: 1.8078937319026657e-05
train Loss: 0.1871 Top-1 Acc: 94.5591 Top-5 Acc: 99.8154
test Loss: 0.3150 Top-1 Acc: 90.4756 Top-5 Acc: 99.2363
resnet-101 - Epoch 87/100
----------
lr: 1.579060052688548e-05
train Loss: 0.1865 Top-1 Acc: 94.5891 Top-5 Acc: 99.8328
test Loss: 0.3098 Top-1 Acc: 90.3137 Top-5 Acc: 99.3276
resnet-101 - Epoch 88/100
----------
lr: 1.3649019742625657e-05
train Loss: 0.1839 Top-1 Acc: 94.5915 Top-5 Acc: 99.8682
test Loss: 0.3222 Top-1 Acc: 90.5835 Top-5 Acc: 99.2198
resnet-101 - Epoch 89/100
----------
lr: 1.1656536753392287e-05
train Loss: 0.1789 Top-1 Acc: 94.9505 Top-5 Acc: 99.8578
test Loss: 0.3238 Top-1 Acc: 90.2183 Top-5 Acc: 99.2861
resnet-101 - Epoch 90/100
----------
lr: 9.815330310080855e-06
train Loss: 0.1747 Top-1 Acc: 95.0878 Top-5 Acc: 99.8702
test Loss: 0.3187 Top-1 Acc: 90.4133 Top-5 Acc: 99.3360
resnet-101 - Epoch 91/100
----------
lr: 8.127413744904804e-06
train Loss: 0.1726 Top-1 Acc: 95.2170 Top-5 Acc: 99.8777
test Loss: 0.3182 Top-1 Acc: 90.6623 Top-5 Acc: 99.3526
resnet-101 - Epoch 92/100
----------
lr: 6.594632769846354e-06
train Loss: 0.1749 Top-1 Acc: 95.1322 Top-5 Acc: 99.8378
test Loss: 0.3202 Top-1 Acc: 90.4922 Top-5 Acc: 99.2529
resnet-101 - Epoch 93/100
----------
lr: 5.218663458397716e-06
train Loss: 0.1703 Top-1 Acc: 95.1965 Top-5 Acc: 99.8603
test Loss: 0.3188 Top-1 Acc: 90.4590 Top-5 Acc: 99.2945
resnet-101 - Epoch 94/100
----------
lr: 4.001010412799139e-06
train Loss: 0.1688 Top-1 Acc: 95.1397 Top-5 Acc: 99.8678
test Loss: 0.3193 Top-1 Acc: 90.5378 Top-5 Acc: 99.2322
resnet-101 - Epoch 95/100
----------
lr: 2.9430051187785967e-06
train Loss: 0.1679 Top-1 Acc: 95.3273 Top-5 Acc: 99.8727
test Loss: 0.3127 Top-1 Acc: 90.5794 Top-5 Acc: 99.2695
resnet-101 - Epoch 96/100
----------
lr: 2.0458044895916517e-06
train Loss: 0.1633 Top-1 Acc: 95.3896 Top-5 Acc: 99.8977
test Loss: 0.3106 Top-1 Acc: 90.4797 Top-5 Acc: 99.2571
resnet-101 - Epoch 97/100
----------
lr: 1.3103896009537207e-06
train Loss: 0.1639 Top-1 Acc: 95.3825 Top-5 Acc: 99.8927
test Loss: 0.3217 Top-1 Acc: 90.4134 Top-5 Acc: 99.2779
resnet-101 - Epoch 98/100
----------
lr: 7.375646182482875e-07
train Loss: 0.1609 Top-1 Acc: 95.6266 Top-5 Acc: 99.8977
test Loss: 0.3275 Top-1 Acc: 90.4424 Top-5 Acc: 99.2405
resnet-101 - Epoch 99/100
----------
lr: 3.2795591718381975e-07
train Loss: 0.1614 Top-1 Acc: 95.6694 Top-5 Acc: 99.8977
test Loss: 0.3131 Top-1 Acc: 90.6458 Top-5 Acc: 99.2571
resnet-101 - Epoch 100/100
----------
lr: 8.201139886109264e-08
train Loss: 0.1633 Top-1 Acc: 95.5197 Top-5 Acc: 99.9002
test Loss: 0.3211 Top-1 Acc: 90.6042 Top-5 Acc: 99.2696
Training resnet-101 complete in 1331m 5s
Best test Top-1 Acc: 90.662346
Best test Top-5 Acc: 99.352577
train resnet-101 done
```