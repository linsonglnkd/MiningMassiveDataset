import os

def VeryClose(s1, s2) :
    words_1 = s1.split()
    words_2 = s2.split()
    if len(words_1) > len(words_2) :
        for i in range(len(words_1)) :
            if (words_1[0:i] + words_1[i+1:len(words_1)]) == words_2 :
                return True
    elif len(words_1) == len(words_2) :
        for i in range(len(words_1)) :
            if (words_1[0:i] + words_1[i+1:len(words_1)]) == (words_2[0:i] + words_2[i+1:len(words_2)]) :
                return True
    else :
        for i in range(len(words_2)) :
            if (words_2[0:i] + words_2[i+1:len(words_2)]) == words_1 :
                return True
    return False

sentence_list = []
occur_list = []
count = 0
num_similar_pair = 0

os.system('date')
for line in open('sentence.nodup') :
    num_occur = int(line.split()[0])
    sentence = line.split()[1:]
    sentence_list.append(' '.join(sentence))
    occur_list.append(num_occur)
    num_similar_pair += num_occur * (num_occur-1) / 2
    if count > 100000000 :
        break
    count += 1

count = 0
for line in open('sentence.pair') :
    s1_id = int(line.split()[0])
    s2_id = int(line.split()[1])
    num_occur_1 = occur_list[s1_id]
    num_occur_2 = occur_list[s2_id]
    #num_similar_pair += (num_occur_1-1)*num_occur_1 / 2
    #num_similar_pair += (num_occur_2-1)*num_occur_2 / 2
    if VeryClose(sentence_list[s1_id], sentence_list[s2_id]) :
         num_similar_pair += num_occur_1 * num_occur_2

print num_similar_pair
os.system('date')
