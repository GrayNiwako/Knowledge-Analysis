# -*- coding: utf8 -*-

import os
import math
import re

Path = os.path.dirname(os.path.realpath(__file__))
f = open(Path + "\\dazuoye_train-A.txt", 'r')
TrainLines = f.readlines()
f.close()

positive_number = 0
negative_number = 0
neutral_number = 0

dataSet = []
label = []
for line in TrainLines:
    temp1 = line.strip('\n').lower()

    temp1 = temp1.replace('\\u2019', '\'')
    temp1 = temp1.replace('\\u002c', ',')
    temp1 = temp1.replace('!', ' ! ')
    temp1 = temp1.replace('?', ' ? ')
    temp1 = temp1.replace(':)', ' emotion1 ')
    temp1 = temp1.replace(';)', ' emotion2 ')
    temp1 = temp1.replace(':-)', ' emotion3 ')
    temp1 = temp1.replace(':o)', ' emotion4 ')
    temp1 = temp1.replace('=)', ' emotion5 ')
    temp1 = temp1.replace(';-)', ' emotion6 ')
    temp1 = temp1.replace(':0)', ' emotion7 ')
    temp1 = temp1.replace(':D', ' emotion8 ')
    temp1 = temp1.replace(':P', ' emotion9 ')
    temp1 = temp1.replace(':(', ' emotion10 ')
    temp1 = temp1.replace(':-(', ' emotion11 ')
    temp1 = temp1.replace('^^', ' emotion12 ')
    temp1 = temp1.replace('^ ^', ' emotion13 ')
    temp1 = temp1.replace('^_^', ' emotion14 ')
    temp1 = temp1.replace(':-O', ' emotion15 ')
    temp1 = temp1.replace('-_-', ' emotion16 ')
    temp1 = temp1.replace('<3333', ' emotion17 ')
    temp1 = temp1.replace('<333', ' emotion18 ')
    temp1 = temp1.replace('<33', ' emotion19 ')
    temp1 = temp1.replace('<3', ' emotion20 ')
    temp1 = temp1.replace('-', ' - ')
    temp1 = temp1.replace('>', ' > ')
    temp1 = temp1.replace('\'', '')
    temp1 = temp1.replace('@', ' @')
    temp1 = temp1.replace('&amp', '&')

    temp2 = re.split('[][():;&/.,*"=< \t\\\]+', temp1)

    if temp2[1] == 'positive':
        positive_number += 1
    elif temp2[1] == 'negative':
        negative_number += 1
    else:
        neutral_number += 1
    label.append(temp2[1])
    dataSet.append(temp2)
twitter_number = positive_number + negative_number + neutral_number

positive_word_dict = {}
negative_word_dict = {}
neutral_word_dict = {}
last_appear_len = {}
for len_num in range(len(dataSet)):
    wordlist = dataSet[len_num][2:]
    for word in wordlist:
        if len(word) == 0:
            continue
        if word[0] == '#' or word == 'RT':
            continue
        if word.find('@') != -1:
            continue

        if word not in positive_word_dict.keys():
            if label[len_num] == 'positive':
                positive_word_dict[word] = 1
                negative_word_dict[word] = 0
                neutral_word_dict[word] = 0
            elif label[len_num] == 'negative':
                positive_word_dict[word] = 0
                negative_word_dict[word] = 1
                neutral_word_dict[word] = 0
            else:
                positive_word_dict[word] = 0
                negative_word_dict[word] = 0
                neutral_word_dict[word] = 1
            last_appear_len[word] = len_num
        else:
            if last_appear_len[word] != len_num:
                if label[len_num] == 'positive':
                    positive_word_dict[word] += 1
                elif label[len_num] == 'negative':
                    negative_word_dict[word] += 1
                else:
                    neutral_word_dict[word] += 1
                last_appear_len[word] = len_num

for key in positive_word_dict:
    if positive_word_dict[key] == 0:
        positive_word_dict[key] = 1 / (positive_number + 1) * 1.0
    else:
        positive_word_dict[key] = positive_word_dict[key] / positive_number * 1.0

for key in negative_word_dict:
    if negative_word_dict[key] == 0:
        negative_word_dict[key] = 1 / (negative_number + 1) * 1.0
    else:
        negative_word_dict[key] = negative_word_dict[key] / negative_number * 1.0

for key in neutral_word_dict:
    if neutral_word_dict[key] == 0:
        neutral_word_dict[key] = 1 / (neutral_number + 1) * 1.0
    else:
        neutral_word_dict[key] = neutral_word_dict[key] / neutral_number * 1.0

f = open(Path + "\\dazuoye_test-A.txt", 'r')
TestLines = f.readlines()
f.close()
fp = open(Path + u"\\10152130122_钱庭涵.txt", 'w')

ID = []
testSet = []
for line in TestLines:
    temp1 = line.strip('\n').lower()

    temp1 = temp1.replace('\\u2019', '\'')
    temp1 = temp1.replace('\\u002c', ',')
    temp1 = temp1.replace('!', ' ! ')
    temp1 = temp1.replace('?', ' ? ')
    temp1 = temp1.replace(':)', ' emotion1 ')
    temp1 = temp1.replace(';)', ' emotion2 ')
    temp1 = temp1.replace(':-)', ' emotion3 ')
    temp1 = temp1.replace(':o)', ' emotion4 ')
    temp1 = temp1.replace('=)', ' emotion5 ')
    temp1 = temp1.replace(';-)', ' emotion6 ')
    temp1 = temp1.replace(':0)', ' emotion7 ')
    temp1 = temp1.replace(':D', ' emotion8 ')
    temp1 = temp1.replace(':P', ' emotion9 ')
    temp1 = temp1.replace(':(', ' emotion10 ')
    temp1 = temp1.replace(':-(', ' emotion11 ')
    temp1 = temp1.replace('^^', ' emotion12 ')
    temp1 = temp1.replace('^ ^', ' emotion13 ')
    temp1 = temp1.replace('^_^', ' emotion14 ')
    temp1 = temp1.replace(':-O', ' emotion15 ')
    temp1 = temp1.replace('-_-', ' emotion16 ')
    temp1 = temp1.replace('<3333', ' emotion17 ')
    temp1 = temp1.replace('<333', ' emotion18 ')
    temp1 = temp1.replace('<33', ' emotion19 ')
    temp1 = temp1.replace('<3', ' emotion20 ')
    temp1 = temp1.replace('-', ' - ')
    temp1 = temp1.replace('>', ' > ')
    temp1 = temp1.replace('\'', '')
    temp1 = temp1.replace('@', ' @')
    temp1 = temp1.replace('&amp', '&')

    temp2 = re.split('[][():;&/.,*"=< \t\\\]+', temp1)

    ID.append(temp2[0])
    temp2 = temp2[1:]
    testSet.append(temp2)

for testlen_num in range(len(testSet)):
    positive_condition_rate = 0
    negative_condition_rate = 0
    neutral_condition_rate = 0
    for word in testSet[testlen_num]:
        if len(word) == 0:
            continue
        if word[0] == '#' or word == 'RT':
            continue
        if word.find('@') != -1:
            continue

        if word not in positive_word_dict.keys():
            positive_condition_rate = positive_condition_rate + math.log(1 / (positive_number + 1) * 1.0)
            negative_condition_rate = negative_condition_rate + math.log(1 / (negative_number + 1) * 1.0)
            neutral_condition_rate = neutral_condition_rate + math.log(1 / (neutral_number + 1) * 1.0)
        else:
            positive_condition_rate = positive_condition_rate + math.log(positive_word_dict[word] * 1.0)
            negative_condition_rate = negative_condition_rate + math.log(negative_word_dict[word] * 1.0)
            neutral_condition_rate = neutral_condition_rate + math.log(neutral_word_dict[word] * 1.0)

    rate1 = math.log(positive_number / twitter_number) + positive_condition_rate
    rate2 = math.log(negative_number / twitter_number) + negative_condition_rate
    rate3 = math.log(neutral_number / twitter_number) + neutral_condition_rate

    fp.write(ID[testlen_num] + ' ')
    if rate1 > rate2:
        if rate1 > rate3:
            fp.write('positive' + '\n')
        else:
            fp.write('neutral' + '\n')
    else:
        if rate2 > rate3:
            fp.write('negative' + '\n')
        else:
            fp.write('neutral' + '\n')
