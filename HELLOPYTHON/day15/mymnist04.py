from keras import layers
from keras import models
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
import numpy as np
from dask.dataframe.core import _emulate

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# print(test_labels[0])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# 신경망에 맞게 바꿔주는 
train_labels = to_categorical(train_labels) # 0~9 숫자를 배열 idx로 표현
test_labels = to_categorical(test_labels)


# 몰라도됨
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# 강화 ( 크게5, 작은 128(?))
model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images)

# print(np.argmax(predictions[0]))


# 틀린 것을 image파일로 저장하기
for idx, label in enumerate(test_labels):
    tmp = np.argmax(predictions[idx])
    if np.argmax(label) != tmp:
        print(idx)
        
        
        
# arr2d_np = np.array(arr2d[0],dtype=np.uint8)
# cv2.imshow('test image',arr2d_np)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
