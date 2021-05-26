import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import cv2
 
cifar10 = datasets.cifar10 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

print(train_labels[0].shape)

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
 
train_images = train_images.reshape((50000, 32, 32, 3))
test_images = test_images.reshape((10000, 32, 32, 3)) # 마지막숫자(rgb의미) = filter = channel 
 
for idx, item in enumerate(train_images):
    cv2.imwrite('cifar_train/{}_{}.jpg'.format(train_labels[idx][0],idx),item)
    if idx == 100:
        break
    
for idx, item in enumerate(test_images):
    cv2.imwrite('cifar_test/{}_{}.jpg'.format(test_labels[idx][0],idx),item)
    if idx == 100:
        break
 