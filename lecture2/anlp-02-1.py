import spacy

path_r = 'anlp-02.txt'
path_w = 'anlp-02-1.txt'

fin = open(path_r, 'r', encoding = "utf_8")
fout = open(path_w, 'w')
# data = fin.readlines()
data = fin.read()

print(data)
nlp = spacy.load('ja_ginza')
doc = nlp(data)
for sent in doc.sents:
    # print(sent)
    data = str(sent) + '<br/>' + '\n'
    print(data)
    for line in data:
        fout.write(line)

fin.close()
fout.close()


