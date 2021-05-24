import cv2
from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
import numpy as np

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images[0])
print(train_labels[0])

arr2d = []
tmp = []

for i in train_images:
    for j in i:
        if j==0:
            tmp.append(0)    
        else:
            tmp.append(255)
    arr2d.append(tmp)

arr2d_np = np.array(arr2d[0],dtype=np.uint8)
cv2.imshow('test image',arr2d_np)
cv2.waitKey(0)
cv2.destroyAllWindows()


