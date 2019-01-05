# -*- coding: utf8 -*-

import os
import math

Path = os.path.dirname(os.path.realpath(__file__))
f = open(Path + "\\spam_train.txt", 'r')
TrainLines = f.readlines()
f.close()

spam_number = 0
normal_number = 0

dataSet = []
for line in TrainLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(' ')
    if temp2[0] == '1':
        spam_number += 1
    else:
        normal_number += 1
    dataSet.append(temp2)
mail_number = spam_number + normal_number

spam_word_dict = {}
normal_word_dict = {}
last_appear_len = {}
for len_num in range(len(dataSet)):
    label = dataSet[len_num][0]
    wordlist = dataSet[len_num][1:]
    for word in wordlist:
        if word not in spam_word_dict.keys():
            if label == '1':
                spam_word_dict[word] = 1
                normal_word_dict[word] = 0
            else:
                spam_word_dict[word] = 0
                normal_word_dict[word] = 1
            last_appear_len[word] = len_num
        else:
            if last_appear_len[word] != len_num:
                if label == '1':
                    spam_word_dict[word] += 1
                else:
                    normal_word_dict[word] += 1
                last_appear_len[word] = len_num

for key in spam_word_dict:
    if spam_word_dict[key] == 0:
        spam_word_dict[key] = 1 / (spam_number + 1) * 1.0
    else:
        spam_word_dict[key] = spam_word_dict[key] / spam_number * 1.0

for key in normal_word_dict:
    if normal_word_dict[key] == 0:
        normal_word_dict[key] = 1 / (normal_number + 1) * 1.0
    else:
        normal_word_dict[key] = normal_word_dict[key] / normal_number * 1.0

f = open(Path + "\\spam_test.txt", 'r')
TestLines = f.readlines()
f.close()
fp = open(Path + u"\\10152130122_钱庭涵.txt", 'w')

testSet = []
for line in TestLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(' ')
    testSet.append(temp2)

for example in testSet:
    spam_condition_rate = 0
    normal_condition_rate = 0
    for word in example:
        if word not in spam_word_dict.keys():
            spam_condition_rate = spam_condition_rate + math.log(1 / (spam_number + 1) * 1.0)
            normal_condition_rate = normal_condition_rate + math.log(1 / (normal_number + 1) * 1.0)
        else:
            spam_condition_rate = spam_condition_rate + math.log(spam_word_dict[word] * 1.0)
            normal_condition_rate = normal_condition_rate + math.log(normal_word_dict[word] * 1.0)
    if math.log(spam_number / mail_number) + spam_condition_rate > math.log(normal_number / mail_number) + normal_condition_rate:
        fp.write('1\n')
    else:
        fp.write('0\n')

fp.close()
