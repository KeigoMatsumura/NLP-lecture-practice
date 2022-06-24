
import sys
from gensim.models import KeyedVectors

if __name__ == "__main__":
    word2vec = KeyedVectors.load_word2vec_format(sys.argv[1])
    
    print("word1 - word2 + word3:")
    print("word1?", end='')
    word1 = input()
    print("word2?", end='')
    word2 = input()

    print("Similarity:" + word2vec.similarity(word1,word2))
    
