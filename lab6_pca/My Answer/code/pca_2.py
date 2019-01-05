# -*- coding: utf8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

Path = os.path.dirname(os.path.realpath(__file__))

f = open(Path + "\\iris.data.txt", 'r')
Lines = f.readlines()
f.close()

Data = []
type = []
for line in Lines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(',')
    type.append(temp2[-1])
    temp2 = temp2[:-1]
    temp2 = [float(temp2[j]) for j in range(len(temp2))]
    Data.append(temp2)

X = np.mat(Data)
average = np.mean(X, axis=0)
X2 = X - average
C = np.cov(X2, rowvar=False)
eigVals, eigVects = np.linalg.eig(C)

k = 2
eigValInd = np.argsort(eigVals)
eigValInd = eigValInd[:-(k+1):-1]
redEigVals = eigVals[eigValInd]
redEigVects = eigVects[:, eigValInd]
lowDDataMat = X2 * redEigVects

resultData = np.matrix.tolist(lowDDataMat)
Flower1_x = []
Flower1_y = []
Flower2_x = []
Flower2_y = []
Flower3_x = []
Flower3_y = []
for i in range(len(type)):
    if type[i] == 'Iris-setosa':
        Flower1_x.append(resultData[i][0])
        Flower1_y.append(resultData[i][1])
    if type[i] == 'Iris-versicolor':
        Flower2_x.append(resultData[i][0])
        Flower2_y.append(resultData[i][1])
    if type[i] == 'Iris-virginica':
        Flower3_x.append(resultData[i][0])
        Flower3_y.append(resultData[i][1])

plt.scatter(Flower1_x, Flower1_y, color='gold', marker='o', linewidths=1, label='Iris-setosa')
plt.scatter(Flower2_x, Flower2_y, color='skyblue', marker='o', linewidths=1, label='Iris-versicolor')
plt.scatter(Flower3_x, Flower3_y, color='pink', marker='o', linewidths=1, label='Iris-virginica')
plt.legend()

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.subplots_adjust(bottom=0.15, left=0.15)
font1 = {'fontsize': 15, 'verticalalignment': 'bottom', 'horizontalalignment': 'center'}
font2 = {'fontsize': 15, 'verticalalignment': 'top', 'horizontalalignment': 'center'}
plt.title('Data distribution scatter plot (2D)', fontdict=font1)
plt.xlabel('eigenvalues_1', fontdict=font2)
plt.ylabel('eigenvalues_2', fontdict=font1)

plt.savefig(Path + u'\\10152130122_钱庭涵_2.png')
# plt.show()

fp = open(Path + u"\\10152130122_钱庭涵_2.txt", 'w')

fp.write(u'降维后的维度 = ' + str(k) + '\n')
tmp = np.matrix.tolist(redEigVals)
fp.write(u'提取的主成分的特征值为 (' + str(tmp[0]) + ', ' + str(tmp[1]) + ')\n')
fp.close()
