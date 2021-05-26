import tensorflow as tf


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

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), # 28,28을 일렬로 세운다는 의미 (flatten)
    tf.keras.layers.Dense(128, activation='relu'), # 중간 신경망
    tf.keras.layers.Dense(10, activation='softmax') # output 신경망
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)


test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)