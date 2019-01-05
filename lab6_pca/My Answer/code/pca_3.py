# -*- coding: utf8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

k = 3
eigValInd = np.argsort(eigVals)
eigValInd = eigValInd[:-(k+1):-1]
redEigVals = eigVals[eigValInd]
redEigVects = eigVects[:, eigValInd]
lowDDataMat = X2 * redEigVects

resultData = np.matrix.tolist(lowDDataMat)
Flower1_x = []
Flower1_y = []
Flower1_z = []
Flower2_x = []
Flower2_y = []
Flower2_z = []
Flower3_x = []
Flower3_y = []
Flower3_z = []
for i in range(len(type)):
    if type[i] == 'Iris-setosa':
        Flower1_x.append(resultData[i][0])
        Flower1_y.append(resultData[i][1])
        Flower1_z.append(resultData[i][2])
    if type[i] == 'Iris-versicolor':
        Flower2_x.append(resultData[i][0])
        Flower2_y.append(resultData[i][1])
        Flower2_z.append(resultData[i][2])
    if type[i] == 'Iris-virginica':
        Flower3_x.append(resultData[i][0])
        Flower3_y.append(resultData[i][1])
        Flower3_z.append(resultData[i][2])

ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(Flower1_x, Flower1_y, Flower1_z, color='gold', marker='o', linewidths=1, label='Iris-setosa')
ax.scatter(Flower2_x, Flower2_y, Flower2_z, color='skyblue', marker='o', linewidths=1, label='Iris-versicolor')
ax.scatter(Flower3_x, Flower3_y, Flower3_z, color='pink', marker='o', linewidths=1, label='Iris-virginica')
ax.legend(bbox_to_anchor=(0.16, 0.96))

plt.subplots_adjust(left=0.15)
font = {'fontsize': 15, 'verticalalignment': 'bottom', 'horizontalalignment': 'center'}
plt.title('Data distribution scatter plot (3D)', fontdict=font)
ax.set_xlabel('eigenvalues_1')
ax.set_ylabel('eigenvalues_2')
ax.set_zlabel('eigenvalues_3')
plt.savefig(Path + u'\\10152130122_钱庭涵_3.png')
# plt.show()

fp = open(Path + u"\\10152130122_钱庭涵_3.txt", 'w')

fp.write(u'降维后的维度 = ' + str(k) + '\n')
tmp = np.matrix.tolist(redEigVals)
fp.write(u'提取的主成分的特征值为 (' + str(tmp[0]) + ', ' + str(tmp[1]) + ', ' + str(tmp[2]) + ')\n')
fp.close()
