
path_r = 'anlp-02-1.txt'
path_w = 'anlp-02-2.txt'

fin = open(path_r, 'r', encoding = "utf_8")
fout = open(path_w, 'w')
# data = fin.readlines()
data = fin.read()
print(data)
data = data.replace('<br/>', '')


# for line in data:
#     data = line.replace('<br/>', '')

for line in data:
    fout.write(line)
print(data)

fin.close()
fout.close()