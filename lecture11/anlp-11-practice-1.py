import gensim
import pickle
import sys

if __name__ == "__main__":
	print("loading " + sys.argv[1])
	word2vec = gensim.models.KeyedVectors.load_word2vec_format(sys.argv[1], binary=False)
	print("loaded " + sys.argv[1])
	print("saving " + sys.argv[2])
	with open(sys.argv[2], "wb") as file:
		pickle.dump(word2vec, file)
	print("saved " + sys.argv[2])
