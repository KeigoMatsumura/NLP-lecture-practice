import sys
from gensim.models import KeyedVectors

if __name__ == "__main__":
    word2vec = KeyedVectors.load_word2vec_format(sys.argv[1])
    # word2vec = KeyedVectors.load_word2vec_format("./jawiki.all_vectors.100d.txt")
    
    print("word1 - word2 + word3:")
    print("word1?", end='')
    word1 = input()
    print("word2?", end='')
    word2 = input()
    print("word3?", end='')
    word3 = input()

    res = word2vec.most_similar_cosmul(positive=[word2,word3],negative=[word1])
    print(res[0])
