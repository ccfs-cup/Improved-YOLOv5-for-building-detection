# Improved-YOLOv5-for-building-detection

# Introduction
This is the code for the article:"An Improved YOLOv5s Model for Building Detection", https://doi.org/10.3390/electronics13112197.

We first collected a building dataset from real scenes and the internet, and applied an improved GridMask data augmentation method to expand the dataset and reduce the impact of occlusion. To make the model lightweight, we pruned the model by the channel pruning method, which decreases the computational costs of the model. Furthermore, we used Mish as the activation function to help the model converge better in sparse training.

# Dataset
The Building Dateset can be attached in the following link:

# Experimental Design
The overall process of building detection method is shown in the following figure, which includes the following steps: (1) Data augmentation is performed on the dataset, and an improved GridMask method is used to introduce random noise for simulating actual occlusion situations. (2) Sparse training is performed on the improved model to make the parameters of the BN layer approach 0. (3) We crop the BN layer parameters according to the pruning rate. (4) We replace the activation function with Mish and compare its effectiveness with different activation functions.

![Figure  8 The Experimental design](https://github.com/ccfs-cup/Improved-YOLOv5-for-building-detection/assets/172787005/9ebc8f37-6639-454d-9b85-4e0c5531329b)

The Pruning method we use is Network Slimming, its implementation in YOLOv5:https://github.com/midasklr/yolov5prune

To replace different activation functions, models/common.py in the original implementation can be replaced to test different activation functions.

# Testing Results
Improved GridMask
![体育馆遮挡测试](https://github.com/ccfs-cup/Improved-YOLOv5-for-building-detection/assets/172787005/ab3b144a-540b-4081-9e7d-86573d7c728c)

Pruning
![10](https://github.com/ccfs-cup/Improved-YOLOv5-for-building-detection/assets/172787005/a3c8a25c-3681-4cff-8724-243228aaae12)

Activation funstions
![11](https://github.com/ccfs-cup/Improved-YOLOv5-for-building-detection/assets/172787005/44554e2a-bb18-44c9-9fdb-f4dd480f3287)




