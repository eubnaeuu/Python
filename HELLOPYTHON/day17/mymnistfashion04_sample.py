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

print(train_images[0].shape)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']



# cv2.imshow('s',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


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

# predictions = model.predict(test_images_refine)

print(test_images_refine.shape)

img = cv2.imread('baji01.jpg', cv2.IMREAD_GRAYSCALE)
img_refine = (255-img) / 255.0
img_refine = cv2.resize(img_refine, dsize=(28, 28), interpolation=cv2.INTER_AREA)
cv2.imwrite('baji01_night.jpg',img_refine)
img_refine = img_refine.reshape(1,28,28)

prediction = model.predict(img_refine)
print(prediction)
print(np.argmax(prediction))

# test_loss, test_acc = model.evaluate(test_images_refine,  test_labels, verbose=2)
# test_loss, test_acc = model.evaluate(img_refine,  0, verbose=2)
# print('\nTest accuracy:', test_acc)
