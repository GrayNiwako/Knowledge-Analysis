# -*- coding: utf8 -*-

import os

Path = os.path.dirname(os.path.realpath(__file__))
f = open(Path + "\\train.txt", 'r')
TrainLines = f.readlines()
f.close()

dataX = []
dataY = []
for line in TrainLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(',')
    dataY.append(float(temp2[-1]))
    temp2 = temp2[:-1]

    if temp2[0] == 'F':
        temp2.append('1')
        temp2.append('0')
        temp2.append('0')
    elif temp2[0] == 'M':
        temp2.append('0')
        temp2.append('1')
        temp2.append('0')
    else:
        temp2.append('0')
        temp2.append('0')
        temp2.append('1')

    temp2 = temp2[1:]
    temp2 = [float(temp2[i]) for i in range(len(temp2))]
    dataX.append(temp2)

epsilon = 0.0001
alpha = 0.01
# count = 0
error_current = 0
error_last = 0
data_num = len(dataX)
x_length = len(dataX[0])

theta = [0 for i in range(x_length)]

while True:
    # count += 1
    for i in range(data_num):
        diff = dataY[i]
        for j in range(x_length):
            diff -= theta[j] * dataX[i][j]
        for j in range(x_length):
            theta[j] += alpha * diff * dataX[i][j]

    error_current = 0
    for i in range(data_num):
        diff = dataY[i]
        for j in range(x_length):
            diff -= theta[j] * dataX[i][j]
        error_current += diff * diff / 2 * 1.0

    if abs(error_current - error_last) < epsilon:
        break
    else:
        error_last = error_current

# print(count)
# for j in range(x_length):
#     print('theta' + str(j) + ' = ' + str(theta[j]))

f = open(Path + "\\test.txt", 'r')
TestLines = f.readlines()
f.close()

testX = []
testY = []
for line in TestLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(',')

    if temp2[0] == 'F':
        temp2.append('1')
        temp2.append('0')
        temp2.append('0')
    elif temp2[0] == 'M':
        temp2.append('0')
        temp2.append('1')
        temp2.append('0')
    else:
        temp2.append('0')
        temp2.append('0')
        temp2.append('1')

    temp2 = temp2[1:]
    temp2 = [float(temp2[i]) for i in range(len(temp2))]
    testX.append(temp2)

test_num = len(testX)
for i in range(test_num):
    y = 0.0
    for j in range(x_length):
        y += theta[j] * testX[i][j]
    testY.append(y)

fp = open(Path + u"\\10152130122_钱庭涵.txt", 'w')
for i in range(test_num):
   fp.write(str(testY[i]) + '\n')
fp.close()
