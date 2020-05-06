
# 训练日志

```
$ python train.py 
densenet_121: 5.731 GFlops - 30.437 MB
resnet-34: 7.349 GFlops - 83.177 MB
{'train': <torch.utils.data.dataloader.DataLoader object at 0x7f90c947a250>, 'test': <torch.utils.data.dataloader.DataLoader object at 0x7f90ca53f0d0>}
{'train': 40058, 'test': 12032}
densenet_121 - Epoch 1/100
----------
lr: 5.9999999999999995e-05
train Loss: 1.6834 Top-1 Acc: 37.9973 Top-5 Acc: 73.7548
test Loss: 1.3687 Top-1 Acc: 49.6472 Top-5 Acc: 85.1344
densenet_121 - Epoch 2/100
----------
lr: 0.00011999999999999999
train Loss: 1.4479 Top-1 Acc: 45.0217 Top-5 Acc: 82.0720
test Loss: 1.2121 Top-1 Acc: 55.7396 Top-5 Acc: 88.5209
densenet_121 - Epoch 3/100
----------
lr: 0.00017999999999999998
train Loss: 1.3046 Top-1 Acc: 50.1027 Top-5 Acc: 86.0216
test Loss: 1.0819 Top-1 Acc: 59.4539 Top-5 Acc: 90.9031
densenet_121 - Epoch 4/100
----------
lr: 0.00023999999999999998
train Loss: 1.2096 Top-1 Acc: 53.8239 Top-5 Acc: 87.7386
test Loss: 1.0269 Top-1 Acc: 63.0229 Top-5 Acc: 93.1732
densenet_121 - Epoch 5/100
----------
lr: 0.0003
/home/lab305/anaconda3/envs/pytorch1.5/lib/python3.7/site-packages/torch/optim/lr_scheduler.py:484: UserWarning: To get the last learning rate computed by the scheduler, please use `get_last_lr()`.
  "please use `get_last_lr()`.", UserWarning)
train Loss: 1.1426 Top-1 Acc: 55.9642 Top-5 Acc: 89.4156
test Loss: 0.9208 Top-1 Acc: 65.2640 Top-5 Acc: 93.8040
densenet_121 - Epoch 6/100
----------
lr: 0.0003
train Loss: 1.0605 Top-1 Acc: 59.0319 Top-5 Acc: 90.6464
test Loss: 0.8532 Top-1 Acc: 67.9076 Top-5 Acc: 93.9409
densenet_121 - Epoch 7/100
----------
lr: 0.0002999453257340926
train Loss: 0.9971 Top-1 Acc: 61.5268 Top-5 Acc: 92.0160
test Loss: 0.7809 Top-1 Acc: 70.0531 Top-5 Acc: 95.2813
densenet_121 - Epoch 8/100
----------
lr: 0.0002997813627218775
train Loss: 0.9456 Top-1 Acc: 63.3069 Top-5 Acc: 92.8230
test Loss: 0.7924 Top-1 Acc: 68.3184 Top-5 Acc: 95.6258
densenet_121 - Epoch 9/100
----------
lr: 0.0002995082902545012
train Loss: 0.9057 Top-1 Acc: 64.7482 Top-5 Acc: 93.3611
test Loss: 0.6822 Top-1 Acc: 73.8836 Top-5 Acc: 96.7214
densenet_121 - Epoch 10/100
----------
lr: 0.0002991264069326976
train Loss: 0.8645 Top-1 Acc: 66.4609 Top-5 Acc: 94.1525
test Loss: 0.6368 Top-1 Acc: 76.1662 Top-5 Acc: 96.9414
densenet_121 - Epoch 11/100
----------
lr: 0.00029863613034027234
train Loss: 0.8230 Top-1 Acc: 68.2074 Top-5 Acc: 94.4469
test Loss: 0.6714 Top-1 Acc: 74.3152 Top-5 Acc: 96.2193
densenet_121 - Epoch 12/100
----------
lr: 0.00029803799658748107
train Loss: 0.7928 Top-1 Acc: 69.1371 Top-5 Acc: 94.8889
test Loss: 0.6254 Top-1 Acc: 75.8134 Top-5 Acc: 97.0659
densenet_121 - Epoch 13/100
----------
lr: 0.00029733265972480075
train Loss: 0.7674 Top-1 Acc: 70.3677 Top-5 Acc: 95.1725
test Loss: 0.5622 Top-1 Acc: 78.3615 Top-5 Acc: 97.3938
densenet_121 - Epoch 14/100
----------
lr: 0.00029652089102773503
train Loss: 0.7436 Top-1 Acc: 71.2245 Top-5 Acc: 95.5094
test Loss: 0.5311 Top-1 Acc: 80.7229 Top-5 Acc: 98.0204
densenet_121 - Epoch 15/100
----------
lr: 0.00029560357815343596
train Loss: 0.7257 Top-1 Acc: 71.8594 Top-5 Acc: 95.7589
test Loss: 0.5017 Top-1 Acc: 82.0551 Top-5 Acc: 97.9415
densenet_121 - Epoch 16/100
----------
lr: 0.0002945817241700637
train Loss: 0.6915 Top-1 Acc: 73.4308 Top-5 Acc: 96.0833
test Loss: 0.5169 Top-1 Acc: 79.9925 Top-5 Acc: 98.0826
densenet_121 - Epoch 17/100
----------
lr: 0.0002934564464599463
train Loss: 0.6813 Top-1 Acc: 73.5813 Top-5 Acc: 96.1588
test Loss: 0.4834 Top-1 Acc: 81.8102 Top-5 Acc: 98.3524
densenet_121 - Epoch 18/100
----------
lr: 0.00029222897549773875
train Loss: 0.6570 Top-1 Acc: 74.6584 Top-5 Acc: 96.5395
test Loss: 0.4875 Top-1 Acc: 82.2834 Top-5 Acc: 98.0951
densenet_121 - Epoch 19/100
----------
lr: 0.00029090065350491655
train Loss: 0.6423 Top-1 Acc: 75.0739 Top-5 Acc: 96.6221
test Loss: 0.4594 Top-1 Acc: 82.9100 Top-5 Acc: 98.2279
densenet_121 - Epoch 20/100
----------
lr: 0.00028947293298207667
train Loss: 0.6215 Top-1 Acc: 76.0307 Top-5 Acc: 96.8589
test Loss: 0.4711 Top-1 Acc: 82.4079 Top-5 Acc: 98.1200
densenet_121 - Epoch 21/100
----------
lr: 0.0002879473751206492
train Loss: 0.6134 Top-1 Acc: 76.3617 Top-5 Acc: 96.7964
test Loss: 0.4374 Top-1 Acc: 83.7027 Top-5 Acc: 98.5474
densenet_121 - Epoch 22/100
----------
lr: 0.0002863256480957577
train Loss: 0.5980 Top-1 Acc: 76.9779 Top-5 Acc: 97.0341
test Loss: 0.4401 Top-1 Acc: 83.6819 Top-5 Acc: 98.5807
densenet_121 - Epoch 23/100
----------
lr: 0.00028460952524209386
train Loss: 0.5871 Top-1 Acc: 77.1914 Top-5 Acc: 97.2055
test Loss: 0.4430 Top-1 Acc: 83.1673 Top-5 Acc: 98.6222
densenet_121 - Epoch 24/100
----------
lr: 0.00028280088311480236
train Loss: 0.5696 Top-1 Acc: 78.0562 Top-5 Acc: 97.3881
test Loss: 0.4331 Top-1 Acc: 83.5367 Top-5 Acc: 98.5889
densenet_121 - Epoch 25/100
----------
lr: 0.0002809016994374951
train Loss: 0.5601 Top-1 Acc: 78.5323 Top-5 Acc: 97.3951
test Loss: 0.4358 Top-1 Acc: 83.4620 Top-5 Acc: 98.2901
densenet_121 - Epoch 26/100
----------
lr: 0.0002789140509396397
train Loss: 0.5529 Top-1 Acc: 78.6358 Top-5 Acc: 97.3977
test Loss: 0.3992 Top-1 Acc: 84.9809 Top-5 Acc: 98.8048
densenet_121 - Epoch 27/100
----------
lr: 0.00027684011108568626
train Loss: 0.5367 Top-1 Acc: 79.2659 Top-5 Acc: 97.6205
test Loss: 0.4011 Top-1 Acc: 85.6325 Top-5 Acc: 98.7715
densenet_121 - Epoch 28/100
----------
lr: 0.0002746821476984157
train Loss: 0.5238 Top-1 Acc: 79.7321 Top-5 Acc: 97.6151
test Loss: 0.3939 Top-1 Acc: 85.6034 Top-5 Acc: 98.7217
densenet_121 - Epoch 29/100
----------
lr: 0.00027244252047910927
train Loss: 0.5106 Top-1 Acc: 80.4311 Top-5 Acc: 97.7075
test Loss: 0.4039 Top-1 Acc: 84.9062 Top-5 Acc: 98.8213
densenet_121 - Epoch 30/100
----------
lr: 0.0002701236784272492
train Loss: 0.5061 Top-1 Acc: 80.4604 Top-5 Acc: 97.8842
test Loss: 0.3780 Top-1 Acc: 86.3919 Top-5 Acc: 98.8463
densenet_121 - Epoch 31/100
----------
lr: 0.00026772815716257447
train Loss: 0.4951 Top-1 Acc: 80.8773 Top-5 Acc: 97.9042
test Loss: 0.3894 Top-1 Acc: 86.0309 Top-5 Acc: 98.6014
densenet_121 - Epoch 32/100
----------
lr: 0.0002652585761524172
train Loss: 0.4829 Top-1 Acc: 81.3129 Top-5 Acc: 98.0268
test Loss: 0.3916 Top-1 Acc: 85.0432 Top-5 Acc: 98.6636
densenet_121 - Epoch 33/100
----------
lr: 0.0002627176358473541
train Loss: 0.4726 Top-1 Acc: 81.6130 Top-5 Acc: 98.1836
test Loss: 0.3651 Top-1 Acc: 86.5414 Top-5 Acc: 98.7549
densenet_121 - Epoch 34/100
----------
lr: 0.0002601081147283029
train Loss: 0.4674 Top-1 Acc: 81.8782 Top-5 Acc: 98.2460
test Loss: 0.3655 Top-1 Acc: 86.2716 Top-5 Acc: 99.0288
densenet_121 - Epoch 35/100
----------
lr: 0.00025743286626829477
train Loss: 0.4480 Top-1 Acc: 82.7726 Top-5 Acc: 98.3283
test Loss: 0.3472 Top-1 Acc: 86.9895 Top-5 Acc: 99.0289
densenet_121 - Epoch 36/100
----------
lr: 0.00025469481581224314
train Loss: 0.4516 Top-1 Acc: 82.6021 Top-5 Acc: 98.2934
test Loss: 0.3600 Top-1 Acc: 86.9481 Top-5 Acc: 99.0372
densenet_121 - Epoch 37/100
----------
lr: 0.00025189695737812197
train Loss: 0.4383 Top-1 Acc: 82.9627 Top-5 Acc: 98.3657
test Loss: 0.3415 Top-1 Acc: 87.6452 Top-5 Acc: 99.0786
densenet_121 - Epoch 38/100
----------
lr: 0.00024904235038305123
train Loss: 0.4332 Top-1 Acc: 83.2017 Top-5 Acc: 98.3831
test Loss: 0.3528 Top-1 Acc: 87.4709 Top-5 Acc: 98.9874
densenet_121 - Epoch 39/100
----------
lr: 0.00024613411629786924
train Loss: 0.4231 Top-1 Acc: 83.6653 Top-5 Acc: 98.5105
test Loss: 0.3470 Top-1 Acc: 86.9024 Top-5 Acc: 98.9210
densenet_121 - Epoch 40/100
----------
lr: 0.00024317543523384976
train Loss: 0.4148 Top-1 Acc: 83.8809 Top-5 Acc: 98.4905
test Loss: 0.3469 Top-1 Acc: 87.3755 Top-5 Acc: 98.8712
densenet_121 - Epoch 41/100
----------
lr: 0.00024016954246529744
train Loss: 0.4056 Top-1 Acc: 84.5112 Top-5 Acc: 98.5130
test Loss: 0.3443 Top-1 Acc: 86.9729 Top-5 Acc: 98.9541
densenet_121 - Epoch 42/100
----------
lr: 0.00023711972489182256
train Loss: 0.3968 Top-1 Acc: 84.7521 Top-5 Acc: 98.5582
test Loss: 0.3504 Top-1 Acc: 86.7904 Top-5 Acc: 98.9085
densenet_121 - Epoch 43/100
----------
lr: 0.00023402931744416478
train Loss: 0.3960 Top-1 Acc: 84.7753 Top-5 Acc: 98.6751
test Loss: 0.3470 Top-1 Acc: 87.0850 Top-5 Acc: 98.9376
densenet_121 - Epoch 44/100
----------
lr: 0.00023090169943749522
train Loss: 0.3799 Top-1 Acc: 85.3829 Top-5 Acc: 98.7375
test Loss: 0.3414 Top-1 Acc: 86.9190 Top-5 Acc: 98.9251
densenet_121 - Epoch 45/100
----------
lr: 0.00022774029087618494
train Loss: 0.3779 Top-1 Acc: 85.5763 Top-5 Acc: 98.7051
test Loss: 0.3246 Top-1 Acc: 87.6535 Top-5 Acc: 98.9666
densenet_121 - Epoch 46/100
----------
lr: 0.0002245485487140804
train Loss: 0.3735 Top-1 Acc: 85.5495 Top-5 Acc: 98.7454
test Loss: 0.3212 Top-1 Acc: 88.0893 Top-5 Acc: 99.0039
densenet_121 - Epoch 47/100
----------
lr: 0.00022132996307437517
train Loss: 0.3652 Top-1 Acc: 85.9572 Top-5 Acc: 98.8277
test Loss: 0.3248 Top-1 Acc: 87.7324 Top-5 Acc: 99.0870
densenet_121 - Epoch 48/100
----------
lr: 0.00021808805343321143
train Loss: 0.3563 Top-1 Acc: 86.2473 Top-5 Acc: 98.8248
test Loss: 0.3288 Top-1 Acc: 88.3757 Top-5 Acc: 99.0247
densenet_121 - Epoch 49/100
----------
lr: 0.00021482636477118463
train Loss: 0.3509 Top-1 Acc: 86.4981 Top-5 Acc: 98.9396
test Loss: 0.3314 Top-1 Acc: 88.1848 Top-5 Acc: 98.9459
densenet_121 - Epoch 50/100
----------
lr: 0.00021154846369695907
train Loss: 0.3430 Top-1 Acc: 86.8369 Top-5 Acc: 98.9770
test Loss: 0.3202 Top-1 Acc: 88.4089 Top-5 Acc: 99.1990
densenet_121 - Epoch 51/100
----------
lr: 0.00020825793454723368
train Loss: 0.3366 Top-1 Acc: 87.1409 Top-5 Acc: 98.9799
test Loss: 0.3240 Top-1 Acc: 88.0105 Top-5 Acc: 98.9044
densenet_121 - Epoch 52/100
----------
lr: 0.00020495837546732266
train Loss: 0.3315 Top-1 Acc: 87.3514 Top-5 Acc: 99.0095
test Loss: 0.3182 Top-1 Acc: 88.2014 Top-5 Acc: 98.9790
densenet_121 - Epoch 53/100
----------
lr: 0.00020165339447663624
train Loss: 0.3258 Top-1 Acc: 87.6359 Top-5 Acc: 99.0144
test Loss: 0.3209 Top-1 Acc: 87.8238 Top-5 Acc: 98.9002
densenet_121 - Epoch 54/100
----------
lr: 0.00019834660552336454
train Loss: 0.3196 Top-1 Acc: 87.7823 Top-5 Acc: 99.0644
test Loss: 0.3172 Top-1 Acc: 88.4296 Top-5 Acc: 99.0081
densenet_121 - Epoch 55/100
----------
lr: 0.00019504162453267814
train Loss: 0.3115 Top-1 Acc: 88.0916 Top-5 Acc: 99.1392
test Loss: 0.3294 Top-1 Acc: 87.5457 Top-5 Acc: 98.8960
densenet_121 - Epoch 56/100
----------
lr: 0.00019174206545276713
train Loss: 0.3105 Top-1 Acc: 87.9644 Top-5 Acc: 99.1916
test Loss: 0.3075 Top-1 Acc: 88.6869 Top-5 Acc: 99.0206
densenet_121 - Epoch 57/100
----------
lr: 0.00018845153630304176
train Loss: 0.3018 Top-1 Acc: 88.4546 Top-5 Acc: 99.0918
test Loss: 0.3150 Top-1 Acc: 88.2927 Top-5 Acc: 98.8919
densenet_121 - Epoch 58/100
----------
lr: 0.00018517363522881612
train Loss: 0.3034 Top-1 Acc: 88.4268 Top-5 Acc: 99.1367
test Loss: 0.3039 Top-1 Acc: 88.6537 Top-5 Acc: 98.9085
densenet_121 - Epoch 59/100
----------
lr: 0.00018191194656678935
train Loss: 0.2944 Top-1 Acc: 88.6256 Top-5 Acc: 99.2390
test Loss: 0.3071 Top-1 Acc: 88.2802 Top-5 Acc: 99.0828
densenet_121 - Epoch 60/100
----------
lr: 0.00017867003692562564
train Loss: 0.2871 Top-1 Acc: 89.0934 Top-5 Acc: 99.2241
test Loss: 0.3013 Top-1 Acc: 88.9692 Top-5 Acc: 98.9791
densenet_121 - Epoch 61/100
----------
lr: 0.0001754514512859204
train Loss: 0.2834 Top-1 Acc: 89.1703 Top-5 Acc: 99.2415
test Loss: 0.2985 Top-1 Acc: 89.1185 Top-5 Acc: 98.9790
densenet_121 - Epoch 62/100
----------
lr: 0.00017225970912381584
train Loss: 0.2754 Top-1 Acc: 89.4627 Top-5 Acc: 99.2390
test Loss: 0.2987 Top-1 Acc: 88.7990 Top-5 Acc: 98.9708
densenet_121 - Epoch 63/100
----------
lr: 0.00016909830056250556
train Loss: 0.2769 Top-1 Acc: 89.4373 Top-5 Acc: 99.2668
test Loss: 0.3019 Top-1 Acc: 88.6371 Top-5 Acc: 99.0704
densenet_121 - Epoch 64/100
----------
lr: 0.00016597068255583595
train Loss: 0.2674 Top-1 Acc: 89.7912 Top-5 Acc: 99.3364
test Loss: 0.3073 Top-1 Acc: 88.3342 Top-5 Acc: 98.9127
densenet_121 - Epoch 65/100
----------
lr: 0.00016288027510817817
train Loss: 0.2616 Top-1 Acc: 90.1608 Top-5 Acc: 99.3712
test Loss: 0.2926 Top-1 Acc: 89.0148 Top-5 Acc: 99.1782
densenet_121 - Epoch 66/100
----------
lr: 0.00015983045753470329
train Loss: 0.2545 Top-1 Acc: 90.3002 Top-5 Acc: 99.4012
test Loss: 0.2950 Top-1 Acc: 88.9484 Top-5 Acc: 99.1617
densenet_121 - Epoch 67/100
----------
lr: 0.00015682456476615093
train Loss: 0.2511 Top-1 Acc: 90.5359 Top-5 Acc: 99.3691
test Loss: 0.3018 Top-1 Acc: 88.4462 Top-5 Acc: 98.9376
densenet_121 - Epoch 68/100
----------
lr: 0.00015386588370213143
train Loss: 0.2474 Top-1 Acc: 90.3426 Top-5 Acc: 99.4090
test Loss: 0.2919 Top-1 Acc: 89.0770 Top-5 Acc: 98.9707
densenet_121 - Epoch 69/100
----------
lr: 0.00015095764961694938
train Loss: 0.2414 Top-1 Acc: 90.9425 Top-5 Acc: 99.4714
test Loss: 0.2964 Top-1 Acc: 89.2472 Top-5 Acc: 98.9624
densenet_121 - Epoch 70/100
----------
lr: 0.00014810304262187867
train Loss: 0.2402 Top-1 Acc: 90.7134 Top-5 Acc: 99.4162
test Loss: 0.3084 Top-1 Acc: 88.5209 Top-5 Acc: 98.8462
densenet_121 - Epoch 71/100
----------
lr: 0.00014530518418775753
train Loss: 0.2284 Top-1 Acc: 91.2943 Top-5 Acc: 99.5085
test Loss: 0.2995 Top-1 Acc: 88.7990 Top-5 Acc: 98.9874
densenet_121 - Epoch 72/100
----------
lr: 0.00014256713373170582
train Loss: 0.2323 Top-1 Acc: 91.1243 Top-5 Acc: 99.5409
test Loss: 0.2949 Top-1 Acc: 89.0313 Top-5 Acc: 99.0040
densenet_121 - Epoch 73/100
----------
lr: 0.00013989188527169767
train Loss: 0.2280 Top-1 Acc: 91.1887 Top-5 Acc: 99.4835
test Loss: 0.2916 Top-1 Acc: 89.2140 Top-5 Acc: 98.9625
densenet_121 - Epoch 74/100
----------
lr: 0.00013728236415264648
train Loss: 0.2189 Top-1 Acc: 91.5676 Top-5 Acc: 99.5709
test Loss: 0.2877 Top-1 Acc: 89.1351 Top-5 Acc: 98.9749
densenet_121 - Epoch 75/100
----------
lr: 0.0001347414238475833
train Loss: 0.2143 Top-1 Acc: 91.7889 Top-5 Acc: 99.5883
test Loss: 0.2909 Top-1 Acc: 88.8529 Top-5 Acc: 99.0081
densenet_121 - Epoch 76/100
----------
lr: 0.00013227184283742607
train Loss: 0.2151 Top-1 Acc: 91.6657 Top-5 Acc: 99.5834
test Loss: 0.2867 Top-1 Acc: 89.1517 Top-5 Acc: 99.1451
densenet_121 - Epoch 77/100
----------
lr: 0.0001298763215727513
train Loss: 0.2095 Top-1 Acc: 92.0250 Top-5 Acc: 99.5937
test Loss: 0.2906 Top-1 Acc: 89.3219 Top-5 Acc: 98.8794
densenet_121 - Epoch 78/100
----------
lr: 0.00012755747952089124
train Loss: 0.2086 Top-1 Acc: 91.9951 Top-5 Acc: 99.5808
test Loss: 0.2875 Top-1 Acc: 89.0189 Top-5 Acc: 99.0579
densenet_121 - Epoch 79/100
----------
lr: 0.00012531785230158478
train Loss: 0.2016 Top-1 Acc: 92.3040 Top-5 Acc: 99.5808
test Loss: 0.2827 Top-1 Acc: 89.4671 Top-5 Acc: 99.1367
densenet_121 - Epoch 80/100
----------
lr: 0.00012315988891431422
train Loss: 0.1966 Top-1 Acc: 92.5478 Top-5 Acc: 99.6033
test Loss: 0.2837 Top-1 Acc: 89.1268 Top-5 Acc: 99.0704
densenet_121 - Epoch 81/100
----------
lr: 0.00012108594906036077
train Loss: 0.1978 Top-1 Acc: 92.6198 Top-5 Acc: 99.5384
test Loss: 0.2883 Top-1 Acc: 89.3053 Top-5 Acc: 98.9791
densenet_121 - Epoch 82/100
----------
lr: 0.00011909830056250538
train Loss: 0.1949 Top-1 Acc: 92.6846 Top-5 Acc: 99.6133
test Loss: 0.2842 Top-1 Acc: 89.4879 Top-5 Acc: 99.1201
densenet_121 - Epoch 83/100
----------
lr: 0.0001171991168851981
train Loss: 0.1924 Top-1 Acc: 92.6825 Top-5 Acc: 99.5957
test Loss: 0.2933 Top-1 Acc: 89.2181 Top-5 Acc: 99.0039
densenet_121 - Epoch 84/100
----------
lr: 0.00011539047475790656
train Loss: 0.1857 Top-1 Acc: 92.8006 Top-5 Acc: 99.6731
test Loss: 0.2861 Top-1 Acc: 89.3509 Top-5 Acc: 99.0537
densenet_121 - Epoch 85/100
----------
lr: 0.0001136743519042427
train Loss: 0.1862 Top-1 Acc: 92.9295 Top-5 Acc: 99.6407
test Loss: 0.2776 Top-1 Acc: 89.8614 Top-5 Acc: 99.0454
densenet_121 - Epoch 86/100
----------
lr: 0.00011205262487935118
train Loss: 0.1827 Top-1 Acc: 93.1502 Top-5 Acc: 99.6631
test Loss: 0.2777 Top-1 Acc: 89.6788 Top-5 Acc: 99.0786
densenet_121 - Epoch 87/100
----------
lr: 0.00011052706701792372
train Loss: 0.1792 Top-1 Acc: 93.1776 Top-5 Acc: 99.6561
test Loss: 0.2774 Top-1 Acc: 89.6788 Top-5 Acc: 99.0621
densenet_121 - Epoch 88/100
----------
lr: 0.00010909934649508383
train Loss: 0.1774 Top-1 Acc: 93.4019 Top-5 Acc: 99.6257
test Loss: 0.2940 Top-1 Acc: 88.6496 Top-5 Acc: 98.9707
densenet_121 - Epoch 89/100
----------
lr: 0.00010777102450226157
train Loss: 0.1750 Top-1 Acc: 93.2947 Top-5 Acc: 99.6756
test Loss: 0.2778 Top-1 Acc: 89.7742 Top-5 Acc: 99.2031
densenet_121 - Epoch 90/100
----------
lr: 0.00010654355354005395
train Loss: 0.1783 Top-1 Acc: 93.2871 Top-5 Acc: 99.6632
test Loss: 0.2774 Top-1 Acc: 89.4921 Top-5 Acc: 99.0330
densenet_121 - Epoch 91/100
----------
lr: 0.00010541827582993658
train Loss: 0.1710 Top-1 Acc: 93.5429 Top-5 Acc: 99.6682
test Loss: 0.2764 Top-1 Acc: 89.7992 Top-5 Acc: 99.0621
densenet_121 - Epoch 92/100
----------
lr: 0.00010439642184656428
train Loss: 0.1665 Top-1 Acc: 93.6477 Top-5 Acc: 99.7480
test Loss: 0.2837 Top-1 Acc: 89.3343 Top-5 Acc: 99.1243
densenet_121 - Epoch 93/100
----------
lr: 0.00010347910897226517
train Loss: 0.1701 Top-1 Acc: 93.4567 Top-5 Acc: 99.6657
test Loss: 0.2799 Top-1 Acc: 89.5294 Top-5 Acc: 99.0205
densenet_121 - Epoch 94/100
----------
lr: 0.00010266734027519945
train Loss: 0.1693 Top-1 Acc: 93.5641 Top-5 Acc: 99.7056
test Loss: 0.2820 Top-1 Acc: 89.1019 Top-5 Acc: 99.1534
densenet_121 - Epoch 95/100
----------
lr: 0.00010196200341251908
train Loss: 0.1626 Top-1 Acc: 93.8235 Top-5 Acc: 99.7480
test Loss: 0.2857 Top-1 Acc: 89.1891 Top-5 Acc: 99.0787
densenet_121 - Epoch 96/100
----------
lr: 0.00010136386965972779
train Loss: 0.1561 Top-1 Acc: 94.1521 Top-5 Acc: 99.6931
test Loss: 0.2876 Top-1 Acc: 88.9940 Top-5 Acc: 99.1534
densenet_121 - Epoch 97/100
----------
lr: 0.0001008735930673025
train Loss: 0.1655 Top-1 Acc: 93.6688 Top-5 Acc: 99.7181
test Loss: 0.2919 Top-1 Acc: 89.0895 Top-5 Acc: 99.0330
densenet_121 - Epoch 98/100
----------
lr: 0.00010049170974549887
train Loss: 0.1590 Top-1 Acc: 93.9308 Top-5 Acc: 99.7305
test Loss: 0.2890 Top-1 Acc: 89.1766 Top-5 Acc: 98.9708
densenet_121 - Epoch 99/100
----------
lr: 0.00010021863727812256
train Loss: 0.1617 Top-1 Acc: 93.8705 Top-5 Acc: 99.7060
test Loss: 0.2829 Top-1 Acc: 89.3427 Top-5 Acc: 99.0953
densenet_121 - Epoch 100/100
----------
lr: 0.0001000546742659074
train Loss: 0.1556 Top-1 Acc: 94.0153 Top-5 Acc: 99.7505
test Loss: 0.2786 Top-1 Acc: 89.2015 Top-5 Acc: 99.0703
Training densenet_121 complete in 844m 52s
Best test Top-1 Acc: 89.861382
Best test Top-5 Acc: 99.203133
train densenet_121 done

resnet-34 - Epoch 1/100
----------
lr: 5.9999999999999995e-05
train Loss: 1.7080 Top-1 Acc: 38.4876 Top-5 Acc: 73.0919
test Loss: 1.3521 Top-1 Acc: 50.1370 Top-5 Acc: 83.8936
resnet-34 - Epoch 2/100
----------
lr: 0.00011999999999999999
train Loss: 1.4660 Top-1 Acc: 45.7376 Top-5 Acc: 81.5202
test Loss: 1.2924 Top-1 Acc: 49.5725 Top-5 Acc: 88.4089
resnet-34 - Epoch 3/100
----------
lr: 0.00017999999999999998
train Loss: 1.3440 Top-1 Acc: 49.6624 Top-5 Acc: 84.6710
test Loss: 1.2308 Top-1 Acc: 55.1668 Top-5 Acc: 89.1600
resnet-34 - Epoch 4/100
----------
lr: 0.00023999999999999998
train Loss: 1.2340 Top-1 Acc: 53.2470 Top-5 Acc: 87.2089
test Loss: 1.0380 Top-1 Acc: 60.5951 Top-5 Acc: 91.7870
resnet-34 - Epoch 5/100
----------
lr: 0.0003
train Loss: 1.1738 Top-1 Acc: 55.2658 Top-5 Acc: 88.5413
test Loss: 1.0218 Top-1 Acc: 62.4170 Top-5 Acc: 89.5045
resnet-34 - Epoch 6/100
----------
lr: 0.0003
train Loss: 1.0944 Top-1 Acc: 58.3383 Top-5 Acc: 90.1014
test Loss: 0.9169 Top-1 Acc: 67.2643 Top-5 Acc: 93.9201
resnet-34 - Epoch 7/100
----------
lr: 0.0002999453257340926
train Loss: 1.0335 Top-1 Acc: 60.3767 Top-5 Acc: 91.2387
test Loss: 0.8206 Top-1 Acc: 68.5466 Top-5 Acc: 93.8786
resnet-34 - Epoch 8/100
----------
lr: 0.0002997813627218775
train Loss: 0.9874 Top-1 Acc: 62.3453 Top-5 Acc: 91.7751
test Loss: 0.7281 Top-1 Acc: 72.5680 Top-5 Acc: 95.9330
resnet-34 - Epoch 9/100
----------
lr: 0.0002995082902545012
train Loss: 0.9349 Top-1 Acc: 64.0617 Top-5 Acc: 92.7869
test Loss: 0.7227 Top-1 Acc: 74.7261 Top-5 Acc: 95.7171
resnet-34 - Epoch 10/100
----------
lr: 0.0002991264069326976
train Loss: 0.9096 Top-1 Acc: 65.0720 Top-5 Acc: 93.1292
test Loss: 0.8184 Top-1 Acc: 69.4140 Top-5 Acc: 93.2811
resnet-34 - Epoch 11/100
----------
lr: 0.00029863613034027234
train Loss: 0.8788 Top-1 Acc: 66.2830 Top-5 Acc: 93.7005
test Loss: 0.6382 Top-1 Acc: 76.5106 Top-5 Acc: 96.9207
resnet-34 - Epoch 12/100
----------
lr: 0.00029803799658748107
train Loss: 0.8417 Top-1 Acc: 67.7134 Top-5 Acc: 94.0694
test Loss: 0.6449 Top-1 Acc: 75.2449 Top-5 Acc: 96.7712
resnet-34 - Epoch 13/100
----------
lr: 0.00029733265972480075
train Loss: 0.8132 Top-1 Acc: 69.0218 Top-5 Acc: 94.5014
test Loss: 0.5651 Top-1 Acc: 78.7599 Top-5 Acc: 97.3108
resnet-34 - Epoch 14/100
----------
lr: 0.00029652089102773503
train Loss: 0.7895 Top-1 Acc: 69.6862 Top-5 Acc: 94.7730
test Loss: 0.6286 Top-1 Acc: 77.4942 Top-5 Acc: 97.2443
resnet-34 - Epoch 15/100
----------
lr: 0.00029560357815343596
train Loss: 0.7642 Top-1 Acc: 70.9083 Top-5 Acc: 95.0427
test Loss: 0.5405 Top-1 Acc: 79.9801 Top-5 Acc: 98.0910
resnet-34 - Epoch 16/100
----------
lr: 0.0002945817241700637
train Loss: 0.7461 Top-1 Acc: 71.0099 Top-5 Acc: 95.3593
test Loss: 0.5355 Top-1 Acc: 81.0923 Top-5 Acc: 97.7631
resnet-34 - Epoch 17/100
----------
lr: 0.0002934564464599463
train Loss: 0.7235 Top-1 Acc: 72.1737 Top-5 Acc: 95.6537
test Loss: 0.5407 Top-1 Acc: 80.4159 Top-5 Acc: 97.8253
resnet-34 - Epoch 18/100
----------
lr: 0.00029222897549773875
train Loss: 0.7099 Top-1 Acc: 72.8217 Top-5 Acc: 95.7335
test Loss: 0.4971 Top-1 Acc: 82.7565 Top-5 Acc: 98.3649
resnet-34 - Epoch 19/100
----------
lr: 0.00029090065350491655
train Loss: 0.6851 Top-1 Acc: 73.7479 Top-5 Acc: 96.0404
test Loss: 0.4898 Top-1 Acc: 81.2915 Top-5 Acc: 98.1740
resnet-34 - Epoch 20/100
----------
lr: 0.00028947293298207667
train Loss: 0.6691 Top-1 Acc: 74.2014 Top-5 Acc: 96.1709
test Loss: 0.4948 Top-1 Acc: 82.4245 Top-5 Acc: 98.0578
resnet-34 - Epoch 21/100
----------
lr: 0.0002879473751206492
train Loss: 0.6560 Top-1 Acc: 74.7424 Top-5 Acc: 96.3627
test Loss: 0.4695 Top-1 Acc: 82.1589 Top-5 Acc: 98.1200
resnet-34 - Epoch 22/100
----------
lr: 0.0002863256480957577
train Loss: 0.6377 Top-1 Acc: 75.4422 Top-5 Acc: 96.4557
test Loss: 0.4624 Top-1 Acc: 82.4120 Top-5 Acc: 98.2486
resnet-34 - Epoch 23/100
----------
lr: 0.00028460952524209386
train Loss: 0.6215 Top-1 Acc: 76.0498 Top-5 Acc: 96.7489
test Loss: 0.4636 Top-1 Acc: 83.0387 Top-5 Acc: 98.0163
resnet-34 - Epoch 24/100
----------
lr: 0.00028280088311480236
train Loss: 0.6084 Top-1 Acc: 76.8040 Top-5 Acc: 96.7897
test Loss: 0.4343 Top-1 Acc: 84.2339 Top-5 Acc: 98.5557
resnet-34 - Epoch 25/100
----------
lr: 0.0002809016994374951
train Loss: 0.5942 Top-1 Acc: 77.1259 Top-5 Acc: 96.8862
test Loss: 0.4305 Top-1 Acc: 84.2878 Top-5 Acc: 98.4478
resnet-34 - Epoch 26/100
----------
lr: 0.0002789140509396397
train Loss: 0.5868 Top-1 Acc: 77.4798 Top-5 Acc: 97.0883
test Loss: 0.4470 Top-1 Acc: 83.0843 Top-5 Acc: 98.3524
resnet-34 - Epoch 27/100
----------
lr: 0.00027684011108568626
train Loss: 0.5712 Top-1 Acc: 78.2213 Top-5 Acc: 97.0014
test Loss: 0.4169 Top-1 Acc: 85.0266 Top-5 Acc: 98.6595
resnet-34 - Epoch 28/100
----------
lr: 0.0002746821476984157
train Loss: 0.5632 Top-1 Acc: 78.3506 Top-5 Acc: 97.2779
test Loss: 0.4447 Top-1 Acc: 82.6610 Top-5 Acc: 98.4147
resnet-34 - Epoch 29/100
----------
lr: 0.00027244252047910927
train Loss: 0.5526 Top-1 Acc: 78.8222 Top-5 Acc: 97.4276
test Loss: 0.4011 Top-1 Acc: 85.4499 Top-5 Acc: 98.7259
resnet-34 - Epoch 30/100
----------
lr: 0.0002701236784272492
train Loss: 0.5370 Top-1 Acc: 79.4523 Top-5 Acc: 97.5174
test Loss: 0.3943 Top-1 Acc: 85.2673 Top-5 Acc: 98.7176
resnet-34 - Epoch 31/100
----------
lr: 0.00026772815716257447
train Loss: 0.5284 Top-1 Acc: 79.6423 Top-5 Acc: 97.5000
test Loss: 0.3937 Top-1 Acc: 85.7528 Top-5 Acc: 98.5558
resnet-34 - Epoch 32/100
----------
lr: 0.0002652585761524172
train Loss: 0.5210 Top-1 Acc: 79.9541 Top-5 Acc: 97.5578
test Loss: 0.3897 Top-1 Acc: 86.1678 Top-5 Acc: 98.7633
resnet-34 - Epoch 33/100
----------
lr: 0.0002627176358473541
train Loss: 0.5079 Top-1 Acc: 80.1920 Top-5 Acc: 97.7444
test Loss: 0.3799 Top-1 Acc: 86.1430 Top-5 Acc: 98.8297
resnet-34 - Epoch 34/100
----------
lr: 0.0002601081147283029
train Loss: 0.5010 Top-1 Acc: 80.6742 Top-5 Acc: 97.8393
test Loss: 0.3844 Top-1 Acc: 85.3088 Top-5 Acc: 98.6678
resnet-34 - Epoch 35/100
----------
lr: 0.00025743286626829477
train Loss: 0.4887 Top-1 Acc: 81.1782 Top-5 Acc: 97.8995
test Loss: 0.3657 Top-1 Acc: 86.4583 Top-5 Acc: 98.8960
resnet-34 - Epoch 36/100
----------
lr: 0.00025469481581224314
train Loss: 0.4776 Top-1 Acc: 81.6005 Top-5 Acc: 98.0514
test Loss: 0.3541 Top-1 Acc: 86.6202 Top-5 Acc: 98.8296
resnet-34 - Epoch 37/100
----------
lr: 0.00025189695737812197
train Loss: 0.4718 Top-1 Acc: 81.7916 Top-5 Acc: 98.0863
test Loss: 0.3570 Top-1 Acc: 86.9232 Top-5 Acc: 98.8296
resnet-34 - Epoch 38/100
----------
lr: 0.00024904235038305123
train Loss: 0.4609 Top-1 Acc: 82.5817 Top-5 Acc: 98.0438
test Loss: 0.3735 Top-1 Acc: 86.5579 Top-5 Acc: 98.8462
resnet-34 - Epoch 39/100
----------
lr: 0.00024613411629786924
train Loss: 0.4551 Top-1 Acc: 82.6887 Top-5 Acc: 98.2140
test Loss: 0.3636 Top-1 Acc: 86.4251 Top-5 Acc: 99.0040
resnet-34 - Epoch 40/100
----------
lr: 0.00024317543523384976
train Loss: 0.4411 Top-1 Acc: 83.2259 Top-5 Acc: 98.2065
test Loss: 0.3670 Top-1 Acc: 86.4957 Top-5 Acc: 98.9624
resnet-34 - Epoch 41/100
----------
lr: 0.00024016954246529744
train Loss: 0.4338 Top-1 Acc: 83.6613 Top-5 Acc: 98.3358
test Loss: 0.3708 Top-1 Acc: 85.9977 Top-5 Acc: 98.9542
resnet-34 - Epoch 42/100
----------
lr: 0.00023711972489182256
train Loss: 0.4267 Top-1 Acc: 83.6646 Top-5 Acc: 98.3757
test Loss: 0.3638 Top-1 Acc: 86.5206 Top-5 Acc: 98.8463
resnet-34 - Epoch 43/100
----------
lr: 0.00023402931744416478
train Loss: 0.4217 Top-1 Acc: 83.9807 Top-5 Acc: 98.4086
test Loss: 0.3558 Top-1 Acc: 87.1722 Top-5 Acc: 98.9707
resnet-34 - Epoch 44/100
----------
lr: 0.00023090169943749522
train Loss: 0.4117 Top-1 Acc: 84.2527 Top-5 Acc: 98.5258
test Loss: 0.3326 Top-1 Acc: 87.7200 Top-5 Acc: 99.0870
resnet-34 - Epoch 45/100
----------
lr: 0.00022774029087618494
train Loss: 0.4050 Top-1 Acc: 84.4323 Top-5 Acc: 98.5711
test Loss: 0.3434 Top-1 Acc: 86.9024 Top-5 Acc: 99.0123
resnet-34 - Epoch 46/100
----------
lr: 0.0002245485487140804
train Loss: 0.3980 Top-1 Acc: 84.9634 Top-5 Acc: 98.5554
test Loss: 0.3288 Top-1 Acc: 87.7656 Top-5 Acc: 99.0703
resnet-34 - Epoch 47/100
----------
lr: 0.00022132996307437517
train Loss: 0.3895 Top-1 Acc: 85.1808 Top-5 Acc: 98.6951
test Loss: 0.3322 Top-1 Acc: 87.7365 Top-5 Acc: 99.0206
resnet-34 - Epoch 48/100
----------
lr: 0.00021808805343321143
train Loss: 0.3795 Top-1 Acc: 85.7069 Top-5 Acc: 98.7176
test Loss: 0.3229 Top-1 Acc: 87.8029 Top-5 Acc: 99.0081
resnet-34 - Epoch 49/100
----------
lr: 0.00021482636477118463
train Loss: 0.3776 Top-1 Acc: 85.7230 Top-5 Acc: 98.7478
test Loss: 0.3361 Top-1 Acc: 87.1472 Top-5 Acc: 98.9957
resnet-34 - Epoch 50/100
----------
lr: 0.00021154846369695907
train Loss: 0.3652 Top-1 Acc: 85.9928 Top-5 Acc: 98.8697
test Loss: 0.3280 Top-1 Acc: 88.2138 Top-5 Acc: 99.0123
resnet-34 - Epoch 51/100
----------
lr: 0.00020825793454723368
train Loss: 0.3622 Top-1 Acc: 86.3709 Top-5 Acc: 98.8198
test Loss: 0.3289 Top-1 Acc: 87.9690 Top-5 Acc: 98.9459
resnet-34 - Epoch 52/100
----------
lr: 0.00020495837546732266
train Loss: 0.3500 Top-1 Acc: 86.8478 Top-5 Acc: 98.8522
test Loss: 0.3132 Top-1 Acc: 88.0893 Top-5 Acc: 99.1534
resnet-34 - Epoch 53/100
----------
lr: 0.00020165339447663624
train Loss: 0.3441 Top-1 Acc: 87.1190 Top-5 Acc: 98.9670
test Loss: 0.3140 Top-1 Acc: 88.7450 Top-5 Acc: 98.9708
resnet-34 - Epoch 54/100
----------
lr: 0.00019834660552336454
train Loss: 0.3371 Top-1 Acc: 87.1191 Top-5 Acc: 98.9321
test Loss: 0.3190 Top-1 Acc: 88.5915 Top-5 Acc: 99.1202
resnet-34 - Epoch 55/100
----------
lr: 0.00019504162453267814
train Loss: 0.3324 Top-1 Acc: 87.4969 Top-5 Acc: 98.9746
test Loss: 0.3121 Top-1 Acc: 88.7242 Top-5 Acc: 99.1119
resnet-34 - Epoch 56/100
----------
lr: 0.00019174206545276713
train Loss: 0.3264 Top-1 Acc: 87.5810 Top-5 Acc: 99.1192
test Loss: 0.3034 Top-1 Acc: 88.6164 Top-5 Acc: 99.0869
resnet-34 - Epoch 57/100
----------
lr: 0.00018845153630304176
train Loss: 0.3205 Top-1 Acc: 87.9652 Top-5 Acc: 99.0822
test Loss: 0.3120 Top-1 Acc: 88.2678 Top-5 Acc: 99.1035
resnet-34 - Epoch 58/100
----------
lr: 0.00018517363522881612
train Loss: 0.3126 Top-1 Acc: 88.2233 Top-5 Acc: 99.0893
test Loss: 0.2982 Top-1 Acc: 88.9318 Top-5 Acc: 99.2198
resnet-34 - Epoch 59/100
----------
lr: 0.00018191194656678935
train Loss: 0.3083 Top-1 Acc: 88.3672 Top-5 Acc: 99.1092
test Loss: 0.2985 Top-1 Acc: 89.0978 Top-5 Acc: 99.0787
resnet-34 - Epoch 60/100
----------
lr: 0.00017867003692562564
train Loss: 0.2988 Top-1 Acc: 88.8701 Top-5 Acc: 99.2244
test Loss: 0.2936 Top-1 Acc: 89.5626 Top-5 Acc: 99.1990
resnet-34 - Epoch 61/100
----------
lr: 0.0001754514512859204
train Loss: 0.2898 Top-1 Acc: 89.1382 Top-5 Acc: 99.1545
test Loss: 0.3035 Top-1 Acc: 88.7824 Top-5 Acc: 99.2157
resnet-34 - Epoch 62/100
----------
lr: 0.00017225970912381584
train Loss: 0.2874 Top-1 Acc: 89.1910 Top-5 Acc: 99.2490
test Loss: 0.2940 Top-1 Acc: 88.7783 Top-5 Acc: 99.1367
resnet-34 - Epoch 63/100
----------
lr: 0.00016909830056250556
train Loss: 0.2849 Top-1 Acc: 89.3225 Top-5 Acc: 99.3064
test Loss: 0.2958 Top-1 Acc: 89.1020 Top-5 Acc: 99.1202
resnet-34 - Epoch 64/100
----------
lr: 0.00016597068255583595
train Loss: 0.2817 Top-1 Acc: 89.4423 Top-5 Acc: 99.2793
test Loss: 0.3203 Top-1 Acc: 88.0893 Top-5 Acc: 98.9127
resnet-34 - Epoch 65/100
----------
lr: 0.00016288027510817817
train Loss: 0.2726 Top-1 Acc: 89.9698 Top-5 Acc: 99.3841
test Loss: 0.3020 Top-1 Acc: 88.7990 Top-5 Acc: 99.0994
resnet-34 - Epoch 66/100
----------
lr: 0.00015983045753470329
train Loss: 0.2679 Top-1 Acc: 89.9929 Top-5 Acc: 99.3837
test Loss: 0.2892 Top-1 Acc: 89.4049 Top-5 Acc: 99.0621
resnet-34 - Epoch 67/100
----------
lr: 0.00015682456476615093
train Loss: 0.2619 Top-1 Acc: 90.2357 Top-5 Acc: 99.3417
test Loss: 0.2932 Top-1 Acc: 88.7907 Top-5 Acc: 99.0953
resnet-34 - Epoch 68/100
----------
lr: 0.00015386588370213143
train Loss: 0.2545 Top-1 Acc: 90.4252 Top-5 Acc: 99.4340
test Loss: 0.2809 Top-1 Acc: 89.5625 Top-5 Acc: 99.2156
resnet-34 - Epoch 69/100
----------
lr: 0.00015095764961694938
train Loss: 0.2553 Top-1 Acc: 90.4549 Top-5 Acc: 99.4264
test Loss: 0.2915 Top-1 Acc: 89.2472 Top-5 Acc: 99.1119
resnet-34 - Epoch 70/100
----------
lr: 0.00014810304262187867
train Loss: 0.2458 Top-1 Acc: 90.9984 Top-5 Acc: 99.4186
test Loss: 0.2867 Top-1 Acc: 88.9733 Top-5 Acc: 99.0828
resnet-34 - Epoch 71/100
----------
lr: 0.00014530518418775753
train Loss: 0.2434 Top-1 Acc: 91.0120 Top-5 Acc: 99.4590
test Loss: 0.2932 Top-1 Acc: 88.7367 Top-5 Acc: 99.1202
resnet-34 - Epoch 72/100
----------
lr: 0.00014256713373170582
train Loss: 0.2382 Top-1 Acc: 91.3513 Top-5 Acc: 99.4386
test Loss: 0.2819 Top-1 Acc: 89.4589 Top-5 Acc: 99.1368
resnet-34 - Epoch 73/100
----------
lr: 0.00013989188527169767
train Loss: 0.2386 Top-1 Acc: 91.1281 Top-5 Acc: 99.4611
test Loss: 0.2822 Top-1 Acc: 89.4588 Top-5 Acc: 99.1534
resnet-34 - Epoch 74/100
----------
lr: 0.00013728236415264648
train Loss: 0.2277 Top-1 Acc: 91.5476 Top-5 Acc: 99.5159
test Loss: 0.2872 Top-1 Acc: 89.5003 Top-5 Acc: 99.0869
resnet-34 - Epoch 75/100
----------
lr: 0.0001347414238475833
train Loss: 0.2284 Top-1 Acc: 91.5626 Top-5 Acc: 99.5014
test Loss: 0.2893 Top-1 Acc: 89.4630 Top-5 Acc: 99.1077
resnet-34 - Epoch 76/100
----------
lr: 0.00013227184283742607
train Loss: 0.2216 Top-1 Acc: 91.8892 Top-5 Acc: 99.5534
test Loss: 0.2889 Top-1 Acc: 89.2970 Top-5 Acc: 98.9790
resnet-34 - Epoch 77/100
----------
lr: 0.0001298763215727513
train Loss: 0.2147 Top-1 Acc: 92.1956 Top-5 Acc: 99.5783
test Loss: 0.2721 Top-1 Acc: 90.2266 Top-5 Acc: 99.1118
resnet-34 - Epoch 78/100
----------
lr: 0.00012755747952089124
train Loss: 0.2098 Top-1 Acc: 92.4430 Top-5 Acc: 99.6282
test Loss: 0.2808 Top-1 Acc: 89.6290 Top-5 Acc: 99.1534
resnet-34 - Epoch 79/100
----------
lr: 0.00012531785230158478
train Loss: 0.2123 Top-1 Acc: 92.2305 Top-5 Acc: 99.5434
test Loss: 0.2695 Top-1 Acc: 90.0523 Top-5 Acc: 99.2198
resnet-34 - Epoch 80/100
----------
lr: 0.00012315988891431422
train Loss: 0.2044 Top-1 Acc: 92.6804 Top-5 Acc: 99.6058
test Loss: 0.2811 Top-1 Acc: 89.5418 Top-5 Acc: 99.1285
resnet-34 - Epoch 81/100
----------
lr: 0.00012108594906036077
train Loss: 0.2027 Top-1 Acc: 92.5428 Top-5 Acc: 99.6158
test Loss: 0.2733 Top-1 Acc: 89.7161 Top-5 Acc: 99.1700
resnet-34 - Epoch 82/100
----------
lr: 0.00011909830056250538
train Loss: 0.1957 Top-1 Acc: 92.9192 Top-5 Acc: 99.6607
test Loss: 0.2770 Top-1 Acc: 89.7078 Top-5 Acc: 99.1866
resnet-34 - Epoch 83/100
----------
lr: 0.0001171991168851981
train Loss: 0.1956 Top-1 Acc: 92.9220 Top-5 Acc: 99.6807
test Loss: 0.2747 Top-1 Acc: 89.8739 Top-5 Acc: 99.2945
resnet-34 - Epoch 84/100
----------
lr: 0.00011539047475790656
train Loss: 0.1921 Top-1 Acc: 93.0322 Top-5 Acc: 99.6207
test Loss: 0.2744 Top-1 Acc: 89.8988 Top-5 Acc: 99.1865
resnet-34 - Epoch 85/100
----------
lr: 0.0001136743519042427
train Loss: 0.1934 Top-1 Acc: 93.0031 Top-5 Acc: 99.6332
test Loss: 0.2778 Top-1 Acc: 89.7286 Top-5 Acc: 99.1949
resnet-34 - Epoch 86/100
----------
lr: 0.00011205262487935118
train Loss: 0.1849 Top-1 Acc: 93.3333 Top-5 Acc: 99.6757
test Loss: 0.2763 Top-1 Acc: 89.7784 Top-5 Acc: 99.1160
resnet-34 - Epoch 87/100
----------
lr: 0.00011052706701792372
train Loss: 0.1828 Top-1 Acc: 93.4339 Top-5 Acc: 99.6906
test Loss: 0.2798 Top-1 Acc: 89.9693 Top-5 Acc: 99.0953
resnet-34 - Epoch 88/100
----------
lr: 0.00010909934649508383
train Loss: 0.1854 Top-1 Acc: 93.1719 Top-5 Acc: 99.6682
test Loss: 0.2714 Top-1 Acc: 89.8614 Top-5 Acc: 99.1699
resnet-34 - Epoch 89/100
----------
lr: 0.00010777102450226157
train Loss: 0.1792 Top-1 Acc: 93.4635 Top-5 Acc: 99.7006
test Loss: 0.2760 Top-1 Acc: 89.6082 Top-5 Acc: 99.1035
resnet-34 - Epoch 90/100
----------
lr: 0.00010654355354005395
train Loss: 0.1750 Top-1 Acc: 93.5761 Top-5 Acc: 99.7380
test Loss: 0.2745 Top-1 Acc: 89.8863 Top-5 Acc: 99.0994
resnet-34 - Epoch 91/100
----------
lr: 0.00010541827582993658
train Loss: 0.1760 Top-1 Acc: 93.6826 Top-5 Acc: 99.7156
test Loss: 0.2693 Top-1 Acc: 89.7784 Top-5 Acc: 99.1658
resnet-34 - Epoch 92/100
----------
lr: 0.00010439642184656428
train Loss: 0.1708 Top-1 Acc: 93.8256 Top-5 Acc: 99.7263
test Loss: 0.2834 Top-1 Acc: 89.2638 Top-5 Acc: 99.1451
resnet-34 - Epoch 93/100
----------
lr: 0.00010347910897226517
train Loss: 0.1683 Top-1 Acc: 93.9578 Top-5 Acc: 99.7334
test Loss: 0.2811 Top-1 Acc: 89.5501 Top-5 Acc: 98.9791
resnet-34 - Epoch 94/100
----------
lr: 0.00010266734027519945
train Loss: 0.1701 Top-1 Acc: 93.8274 Top-5 Acc: 99.7230
test Loss: 0.2742 Top-1 Acc: 90.0150 Top-5 Acc: 99.0372
resnet-34 - Epoch 95/100
----------
lr: 0.00010196200341251908
train Loss: 0.1728 Top-1 Acc: 93.8052 Top-5 Acc: 99.7181
test Loss: 0.2632 Top-1 Acc: 90.4964 Top-5 Acc: 99.1783
resnet-34 - Epoch 96/100
----------
lr: 0.00010136386965972779
train Loss: 0.1637 Top-1 Acc: 94.1154 Top-5 Acc: 99.7480
test Loss: 0.2782 Top-1 Acc: 89.7494 Top-5 Acc: 99.1036
resnet-34 - Epoch 97/100
----------
lr: 0.0001008735930673025
train Loss: 0.1607 Top-1 Acc: 94.2622 Top-5 Acc: 99.7480
test Loss: 0.2752 Top-1 Acc: 90.1311 Top-5 Acc: 99.0413
resnet-34 - Epoch 98/100
----------
lr: 0.00010049170974549887
train Loss: 0.1609 Top-1 Acc: 94.1995 Top-5 Acc: 99.7679
test Loss: 0.2707 Top-1 Acc: 89.8158 Top-5 Acc: 99.1035
resnet-34 - Epoch 99/100
----------
lr: 0.00010021863727812256
train Loss: 0.1648 Top-1 Acc: 94.0003 Top-5 Acc: 99.7230
test Loss: 0.2688 Top-1 Acc: 90.1228 Top-5 Acc: 99.1949
resnet-34 - Epoch 100/100
----------
lr: 0.0001000546742659074
train Loss: 0.1597 Top-1 Acc: 94.1999 Top-5 Acc: 99.7555
test Loss: 0.2836 Top-1 Acc: 89.6622 Top-5 Acc: 99.0372
Training resnet-34 complete in 491m 59s
Best test Top-1 Acc: 90.496353
Best test Top-5 Acc: 99.294495
train resnet-34 done
```