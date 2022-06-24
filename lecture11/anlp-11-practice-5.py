from sklearn.model_selection import train_test_split
import numpy as np
import pickle
import sys
import tensorflow as tf

vectorMagnitude = 100
sequenceLength = 100

def text2seq(word2vec, words):
	seq = [[0] * vectorMagnitude] * sequenceLength
	for i in range(len(words)):
		word = words[i]
		if word in word2vec.vocab:
			vec = word2vec.get_vector(word)
			seq[i] = vec
	return seq

if __name__ == "__main__":
	print("reading " + sys.argv[1])
	word2vec = None
	with open(sys.argv[1], "rb") as file:
		word2vec = pickle.load(file)
	print("read " + sys.argv[1])
	print("reading " + sys.argv[2])
	dataFilePath = sys.argv[2]
	seqs = []
	polarities = []
	with open(dataFilePath) as file:
		for line in file.readlines():
			parts = line.split("\t")
			polarity = float(parts[0])
			polarities.append(polarity)
			seq = text2seq(word2vec, parts[1:])
			seqs.append(seq)
	print("read " + sys.argv[2])
	x = np.array(seqs)
	y = np.array(polarities)
	xTrain, xTest, yTrain, yTest = train_test_split(x, y)
	model = tf.keras.models.Sequential()
	model.add(tf.keras.layers.LSTM(50))
	#model.add(tf.keras.layers.Dense(100))
	model.add(tf.keras.layers.Dense(3))
	model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
	history = model.fit(xTrain, yTrain, epochs=5, verbose=1)
	lossTest, accTest = model.evaluate(xTest, yTest)
	print(lossTest, accTest)
	#model.save('model.h5')
	#model = keras.models.load_model('model.h5')
