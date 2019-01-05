# -*- coding: utf8 -*-

import os
import math

Path = os.path.dirname(os.path.realpath(__file__))
f = open(Path + "\\Training.txt", 'r')
TrainLines = f.readlines()
f.close()

dataX = []
dataY = []
for line in TrainLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split('\t')
    dataY.append(float(temp2[-1]))
    temp2 = temp2[:-1]
    temp2 = [float(temp2[i]) for i in range(len(temp2))]
    dataX.append(temp2)

max_data = []
min_data = []
for i in range(21):
    max_data.append(max([line[i] for line in dataX]))
    min_data.append(min([line[i] for line in dataX]))

alpha = 0.0001
count = 2000
loss_function = 0
data_num = len(dataX)
x_length = len(dataX[0])

for line in dataX:
    for i in range(x_length):
        line[i] = line[i] / (max_data[i] - min_data[i]) * 1.0

theta = [1 for i in range(x_length)]

while True:

    for i in range(data_num):
        thetaTx = 0
        for j in range(x_length):
            thetaTx += theta[j] * dataX[i][j]
        h_theta = 1. / (1 + math.exp(-thetaTx))
        for j in range(x_length):
            theta[j] += alpha * (dataY[i] - h_theta) * dataX[i][j]

    for i in range(data_num):
        thetaTx = 0
        for j in range(x_length):
            thetaTx += theta[j] * dataX[i][j]
        h_theta = 1. / (1 + math.exp(-thetaTx))
        if h_theta < 1:
            loss_function += dataY[i] * math.log(abs(h_theta)) + (1 - dataY[i]) * math.log(abs(1 - h_theta))
    loss_function = - loss_function / data_num * 1.0

    count -= 1
    if count == 0:
        break

# for j in range(x_length):
#     print('theta' + str(j) + ' = ' + str(theta[j]))

f = open(Path + "\\Test.txt", 'r')
TestLines = f.readlines()
f.close()

testX = []
testY = []
answer = []
for line in TestLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split('\t')
    answer.append(float(temp2[-1]))
    temp2 = temp2[:-1]
    temp2 = [float(temp2[i]) for i in range(len(temp2))]
    testX.append(temp2)

max_testdata = []
min_testdata = []
for i in range(21):
    max_testdata.append(max([line[i] for line in testX]))
    min_testdata.append(min([line[i] for line in testX]))

test_num = len(testX)

for line in testX:
    for i in range(x_length):
        line[i] = line[i] / (max_testdata[i] - min_testdata[i]) * 1.0

for i in range(test_num):
    thetaTx = 0
    for j in range(x_length):
        thetaTx += theta[j] * testX[i][j]
    h_theta = 1. / (1 + math.exp(-thetaTx))
    if h_theta > 0.5:
        testY.append(1)
    else:
        testY.append(0)

fp = open(Path + u"\\10152130122_钱庭涵.txt", 'w')
for i in range(test_num):
   fp.write(str(testY[i]) + '\n')
fp.close()

# equal = 0
# unequal = 0
# for i in range(test_num):
#     if testY[i] == answer[i]:
#         equal += 1
#     else:
#         unequal += 1
# print('equal = ' + str(equal))
# print('unequal = ' + str(unequal))
# print('rate = ' + str(equal / test_num * 1.0))