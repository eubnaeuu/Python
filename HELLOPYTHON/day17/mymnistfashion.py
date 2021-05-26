import tensorflow as tf
import numpy as np


# 1. Fashion MNIST 데이터셋 불러오기
print("1. Fashion MNIST 데이터셋 불러오기")
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Fashion MNIST 데이터셋 살펴보기
# print(train_images[0])
# print(train_labels[0])

# print(train_images.shape)
# print(train_labels.shape)
# print(test_images.shape)
# print(test_labels.shape)

# 2. 데이터 전처리
print("2.데이터 전처리")
train_images, test_images = train_images / 255.0, test_images / 255.0

# 3. 모델 구성
print("2.모델 구성")
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
print("4.모델 컴파일")
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# 5. 모델 훈련
print("5. 모델 훈련")
model.fit(train_images, train_labels, epochs=5)

# 6. 정확도 평가하기
print("6. 정확도 평가하기")
loss, accuracy = model.evaluate(test_images, test_labels)
print(loss, accuracy)

# 7. 예측하기
print("7. 예측하기")
predictions = model.predict(test_images)
print(predictions[0])
print(np.argmax(predictions[0]))