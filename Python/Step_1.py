import os
os.system('date')

dict = {}
count = 0
for line in open('sentence.nodup') :
    words = line.split()[1:]
    num_occur = line.split()[0]
    line_id = count
    num_words = len(words)
    # create 6 tuples: num_words-1, num_words, num_words+1 plus the first and last 5 words
    for i in range(num_words-1, num_words+2) :
        list_1 = words[:5]
        list_2 = words[-5:]
        list_1.append(i)
        list_2.append(i)
        tuple_1 = tuple(list_1)
        tuple_2 = tuple(list_2)
        hash_1 = str(hash(tuple_1))
        hash_2 = str(hash(tuple_2))
        if not dict.has_key(hash_1) :
            dict[hash_1] = []
        if not dict.has_key(hash_2) :
            dict[hash_2] = []
        dict[hash_1].append(line_id)
        if hash_2 <> hash_1 :
            dict[hash_2].append(line_id)
    if count > 10000000 :
        break
    count += 1
print count
print len(dict)
os.system('date')

f_out = open('sentence.calculate','w')
for key in dict :
    if len(dict[key]) > 1 :
        str1 = [str(x) for x in dict[key]]
        f_out.write(' '.join(str1)+'\n')

f_out.close()
print count
os.system('date')
