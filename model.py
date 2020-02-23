# #!/usr/bin/env python
# # coding: utf-8

# from keras.datasets import mnist
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# # Let's look at the training data.
# train_images.shape
# len(train_labels)
# train_labels

# # Now, let's look at the test data.
# test_images.shape
# len(test_labels)
# test_labels

# # We'll feed the neural network the training data, train_images and train_labels. The network will learn to associate images and labels.
# # Now, let's build the network. Here is the network architecture:
# from keras import models
# from keras import layers

# network = models.Sequential()
# network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# network.add(layers.Dense(10, activation='softmax'))

# # Now, the compilation step.
# network.compile(optimizer='rmsprop',
# loss='categorical_crossentropy',
# metrics=['accuracy'])

# # Let's reshape our image data.
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype('float32') / 255

# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype('float32') / 255

# # We need to categorically encode the labels.
# from keras.utils import to_categorical

# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)

# # We're now going to train teh network, by calling the fit method to fit the model to the training data.
# network.fit(train_images, train_labels, epochs=5, batch_size=128)

# # Let's check the model's performance on the test set.
# test_loss, test_acc = network.evaluate(test_images, test_labels)
# print('test_acc:', test_acc)
