import MeCab
import re
import sys

def excludeTag(text):
	return re.sub(r"<[a-zA-Z0-9_]+\s*/?>", "", text)

def replaceEntity(text):
	replacedText = text
	replacedText = re.sub(r"&apos;", "'", replacedText)
	replacedText = re.sub(r"&quot;", "\"", replacedText)
	replacedText = re.sub(r"&amp;", ">", replacedText)
	replacedText = re.sub(r"&lt;", "<", replacedText)
	replacedText = re.sub(r"&gt;", ">", replacedText)
	return replacedText

def text2words(text):
	words = []
	node = mecab.parseToNode(text)
	while node:
		features = node.feature.split(",")
		word = features[6]
		words.append(word)
		node = node.next
	return words

if __name__ == "__main__":
	mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
	dataFilePath = sys.argv[1]
	with open(dataFilePath) as file:
		file.readline()
		for line in file.readlines():
			parts = line.split("\t")
			star = int(parts[7])
			text = parts[13]
			polarity = None
			if star <= 2:
				polarity = 0
			elif star == 3:
				polarity = 1
			elif star == 5:
				polarity = 2
			if polarity != None:
				text = excludeTag(text)
				words = text2words(text)
				if len(words) <= 100:
					print("{}\t{}".format(str(polarity), "\t".join(words)))
