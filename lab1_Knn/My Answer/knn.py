# -*- coding: utf8 -*- 
import os
import math

K=10;

Path = os.path.dirname(os.path.realpath(__file__))

#将train.txt中的数据读入到TrainData二维列表中

f = open(Path + "\\train.txt", 'r')

TrainLines = f.readlines()
f.close()
TrainData = []

for line in TrainLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(',')
    temp2.append('0')
    TrainData.append(temp2)
    
TrainNumber = len(TrainData)

#创建并打开输出结果文件

fp = open(Path + "\\test_output.txt", 'w')

#打开test.txt，开始处理数据
    
f = open(Path + "\\test.txt", 'r')
    
TestLines = f.readlines()
f.close()

for line in TestLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(',')
    
    num = 0
    setosa_num = 0
    versicolor_num = 0
    virginica_num = 0
    
    while num < TrainNumber:
        a1 = float(temp2[0]) - float(TrainData[num][0])
        a2 = float(temp2[1]) - float(TrainData[num][1])
        a3 = float(temp2[2]) - float(TrainData[num][2])
        a4 = float(temp2[3]) - float(TrainData[num][3])
        dis = math.sqrt(a1*a1 + a2*a2 + a3*a3 + a4*a4)
        TrainData[num][5] = dis
        num = num + 1
        
    for i in range(0, TrainNumber):
        for j in range(i + 1, TrainNumber):
            if float(TrainData[i][5]) >  float(TrainData[j][5]):
                TrainData[i], TrainData[j] = TrainData[j], TrainData[i]
            
    for i in range(0, K):
        if TrainData[i][4] == 'Iris-setosa':
            setosa_num = setosa_num + 1
        if TrainData[i][4] == 'Iris-versicolor':
            versicolor_num = versicolor_num + 1
        if TrainData[i][4] == 'Iris-virginica':
            virginica_num = virginica_num + 1
        
    if setosa_num >= versicolor_num:
        if setosa_num >= virginica_num:
            tmp = 'Iris-setosa'
        else:
            tmp = 'Iris-virginica'
    elif versicolor_num >= virginica_num:
        tmp = 'Iris-versicolor'
    else:
        tmp = 'Iris-virginica'
    temp2.append(tmp)
        
    for i in range(4):
        fp.write(temp2[i] + ',')
    fp.write(temp2[4] + '\n')
    
fp.close()