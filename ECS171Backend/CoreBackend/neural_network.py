# Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization, LeakyReLU
import keras

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from extra_keras_datasets import emnist


from image_processing import process_image
import cv2

# Create dict for decoding array
import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
output_dict = {
	'0': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9
}
for i, j in enumerate(range(10, 36)):
	output_dict[str(j)] = alphabet_lower[i]
for i, j in enumerate(range(36, 62)):
	output_dict[str(j)] = alphabet_upper[i]

def load_data(type='byclass', out_dim=62):
	(train_x, train_y), (test_x, test_y) = emnist.load_data(type=type)
	# Shuffle data to avoid fitting to a specific pattern
	train_x, train_y = shuffle(train_x, train_y, random_state=42)
	test_x, test_y   = shuffle(test_x, test_y, random_state=42)
	# Reshape data to match input shape (# samples, 28, 28, 1)
	train_samples = len(train_x)
	test_samples  = len(test_x)
	num_pixels    = len(train_x[0])
	train_shape   = (train_samples, num_pixels, num_pixels, 1)
	test_shape    = (test_samples,  num_pixels, num_pixels, 1)

	train_x       = np.reshape(train_x, train_shape)
	test_x        = np.reshape(test_x,  test_shape)
	# One hot encode output vectors
	train_y       = keras.utils.to_categorical(train_y, out_dim)
	test_y        = keras.utils.to_categorical(test_y,  out_dim)
	# # Normalize input datas // Scale up data to maybe set apart outliers
	# train_x       = train_x * 45.0 # / 255.0
	# test_x        = test_x  * 45.0 # / 255.0

	return train_x, train_y, test_x, test_y

def decode(encoded_predictions):
	decoder = np.arange(62, dtype=int)
	predictions = encoded_predictions.dot(decoder).astype(int).astype('str')
	for i in range(len(predictions)):
		predictions[i] = output_dict[predictions[i]]
	return predictions

def test_model(model_path, test_input):
	true = ['J', 'O', 'H', 'N', ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ', '4', \
	'2', 'M','S', 'M', 'I', 'T', 'H',  ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ',  ' ', ' ', ' ', \
	'0', '6', '0', '4', '2', '0', '2', '0','1', '6', '0', '0', ' ', 'P', 'e', 'n', 'n', 's', 'y', 'l', 'v', 'a', \
	'n', 'i', 'a', ' ', 'A', 'v', ' ', 'N', 'W', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', \
			' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', 'w', 'a',\
	's', 'h', 'i', 'n', 'g', 't', 'o', 'n', '', 'D', 'C', '', '', '', '', '', '', '', 'D', 'C', '9', '5', '6', '1', '6',\
	'1', '3', '9', '', '', 'N', 'Y']
	model = keras.models.load_model(model_path)
	predictions = decode(np.round(model.predict(test_input)))
	df = pd.DataFrame([predictions,true])
	df.to_csv("predictions.csv")
	print(df.head())
	return predictions

if __name__ == '__main__':
	# emnist_type = 'byclass'
	# out_dim = 62
	# train_losses = []
	# train_accs = []
	# eval_losses = []
	# eval_acss = []
	# train_x, train_y, test_x, test_y = load_data(emnist_type, out_dim)

	# model, train_losses, train_accs, eval_losses, eval_accs = train_model(emnist_type, train_x, train_y, test_x, test_y)
	# test_loss, test_acc = evaluate_model(model, test_x, test_y)
	# print("\nTest Loss: %0.4f, Test Accuracy: %0.4f\n" %(test_loss, test_acc))
	# model.save('model_3')
	# plt = plot_metrics(train_losses, train_accs, eval_losses, eval_accs)
	# plt.show()
	# model = create_model(input_shape=(28, 28, 1), out_dim=62)

	# train_x, train_y, _, _ = load_data()

	# test_x = process_image('IMG_2325.JPG')
	test_x = process_image('image0.jpg')
	test_x = np.array(test_x)

	# cv2.imshow('train', np.concatenate(train_x[0:5]))
	# cv2.imshow('boxes', np.concatenate(test_x[0:5]))
	# cv2.waitKey(0)

	predictions = test_model('model_1', test_x)
