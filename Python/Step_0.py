# remove duplicates

import os
import sys

os.system('date')

count = 0
dict = {}

for line in open('sentences.txt') :
    words = line.split()
    id = words[0]
    sentence = ' '.join(words[1:])
    if not dict.has_key(sentence) :
        dict[sentence] = 1
    else :
        dict[sentence] += 1
    count += 1
    if count > 10000000 :
      break
print count

f_out = open('sentence.nodup','w')
for key in dict :
    str_out=str(dict[key])+ ' ' + key
    f_out.write(str_out+'\n')
f_out.close()
os.system('date')
