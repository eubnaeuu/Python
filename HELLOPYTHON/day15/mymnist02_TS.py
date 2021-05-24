import cv2
from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
import numpy as np

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images[0])
print(train_labels[0])

for idx, img in enumerate(test_images):
    cv2.imwrite('test/{}_{}.jpg'.format(test_labels[idx],idx),img)
    if idx > 100:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()


