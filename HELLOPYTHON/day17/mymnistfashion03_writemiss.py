import tensorflow as tf
import numpy as np
import cv2


fashion_mnist = tf.keras.datasets.fashion_mnist
"""
[자주 쓰이는 것들]

tf.keras.datasets.cifar10 
tf.keras.datasets.imdb
tf.keras.datasets.boston_housing
"""
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images_refine = train_images / 255.0
test_images_refine = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), # 28,28을 일렬로 세운다는 의미 (flatten)
    tf.keras.layers.Dense(128, activation='relu'), # 중간 신경망
    tf.keras.layers.Dense(10, activation='softmax') # output 신경망
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images_refine, train_labels, epochs=10)

predictions = model.predict(test_images_refine)

print(predictions[0])
print(np.argmax(predictions[0]))

cnt_o = 0
cnt_x = 0
for idx, item in enumerate(predictions):
    if np.argmax(item) == test_labels[idx]:
        cnt_o += 1
    else :
        cnt_x += 1
        cv2.imwrite('image_miss/[{}]_[{}]_{}.jpg'.format(test_labels[idx],np.argmax(item),idx),test_images[idx])

print('O : ',cnt_o,', X : ',cnt_x)

# cnt_o = 0
# cnt_x = 0
# for idx, item in enumerate(test_labels) :
#     compred = np.argmax(predictions[idx])
#     if item == compred:
#         cnt_o += 1
#     else :
#         cnt_x += 1
#         cv2.imwrite('image_miss/label[{}]_compred[{}]_{}.jpg'.format(item,compred,idx),test_images[idx])
#
# print('O : ',cnt_o,', X : ',cnt_x)




test_loss, test_acc = model.evaluate(test_images_refine,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)