import MeCab
import sys

if __name__ == "__main__":
	mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
	text = sys.argv[1]
	node = mecab.parseToNode(text)
	while node:
		print("{},{}".format(node.surface, node.feature))
		node = node.next
    list = []
    list.append(text)

    print(list)
