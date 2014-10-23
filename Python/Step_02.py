# generate the pairs
import os

os.system('date')
count = 0
f_out = open('sentence.pair','w')
dict = {}
for line in open('sentence.calculate') :
    words = line.split()
    for i in range(len(words)) :
        for j in range(i+1, len(words)) :
            tmpStr = words[i] + ' ' + words[j]
            if not dict.has_key(tmpStr) :
                dict[tmpStr] = 1
    if count > 100000000 :
        break
    count += 1

for key in dict :
    f_out.write(key+'\n')

f_out.close()
os.system('date')
