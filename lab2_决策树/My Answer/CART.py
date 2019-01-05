# -*- coding: utf8 -*- 

from numpy import *
import os
from math import ceil
import copy


# 计算数据集的Gini指数
def calcGini(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 给所有可能分类创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    Gini = 1.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        Gini -= prob * prob
    return Gini

# 对变量划分数据集
def splitDataSet(dataSet, feature, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[feature] == value:
            reducedFeatVec = featVec[:feature]
            reducedFeatVec.extend(featVec[feature + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet, labels):
    numFeatures = len(dataSet[0]) - 1
    bestGiniIndex = 100000.0
    bestFeature = -1
    bestSplitDict = {}

    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueFeat = set(featList)
        newGiniIndex = 0.0
        # 计算该特征下每种划分的信息熵
        for value in uniqueFeat:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newGiniIndex += prob * calcGini(subDataSet)
        GiniIndex = newGiniIndex
        if GiniIndex < bestGiniIndex:
            bestGiniIndex = GiniIndex
            bestFeature = i
    return bestFeature

# 特征若已经划分完，节点下的样本还没有统一取值，则需要进行投票
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    return max(classCount)


# 递归产生决策树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]

    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet, labels)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel : {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)

    # 针对bestFeat的每个取值，划分出一个子树。
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


# 使用决策树执行分类
def classify(inputTree, featLabels, testVec):
    global classLabel
    firstSides = list(inputTree.keys())
    firstStr = firstSides[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)

    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]) == dict:
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


# 测试决策树正确率
def testing(myTree, data_test, labels):
    error = 0.0
    for i in range(len(data_test)):
        if classify(myTree, labels, data_test[i]) != data_test[i][-1]:
            error += 1
    return float(error)


# 测试投票节点正确率
def testingMajor(major, data_test):
    error = 0.0
    for i in range(len(data_test)):
        if major != data_test[i][-1]:
            error += 1
    return float(error)


# 剪枝
def postPruningTree(inputTree, dataSet, data_test, labels):
    firstSides = list(inputTree.keys())
    firstStr = firstSides[0]
    secondDict = inputTree[firstStr]
    classList = [example[-1] for example in dataSet]
    featkey = copy.deepcopy(firstStr)
    labelIndex = labels.index(featkey)
    temp_labels = copy.deepcopy(labels)
    del(labels[labelIndex])

    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            inputTree[firstStr][key] = postPruningTree(secondDict[key],\
            splitDataSet(dataSet, labelIndex, key), splitDataSet(data_test, labelIndex, key), copy.deepcopy(labels))

    if testing(inputTree, data_test, temp_labels) <= testingMajor(majorityCnt(classList), data_test):
        return inputTree
    return majorityCnt(classList)


classLabel = -1
Path = os.path.dirname(os.path.realpath(__file__))
f = open(Path + "\\spam-train.data", 'r')
TrainLines = f.readlines()
f.close()
dataSet = []
for line in TrainLines:
    temp1 = line.strip('\n')
    temp2 = temp1.split(' ')
    temp2 = temp2[1:]
    for i in range(58):
        temp2[i] = float(temp2[i])
    dataSet.append(temp2)

labels = []
for i in range(57):
    temp3 = 'number' + str(i + 1)
    labels.append(temp3)
labels_copy1 = labels[:]
labels_copy2 = labels[:]

cartTree = createTree(dataSet, labels)
cartTree = postPruningTree(cartTree, dataSet, dataSet, labels_copy1)

# test data
f = open(Path + "\\spam-test.data", 'r')
TestLines = f.readlines()
f.close()

testdata = []
testID = []
for line in TestLines:
   temp1 = line.strip('\n')
   temp2 = temp1.split(' ')
   testID.append(temp2[0])
   temp2 = temp2[1:]
   for i in range(57):
       temp2[i] = float(temp2[i])
   testdata.append(temp2)

fp = open(Path + "\\spam-test_output.data", 'w')

for i in range(len(testdata)):
   result = classify(cartTree, labels_copy2, testdata[i])
   re = int(ceil(result))
   fp.write(testID[i] + ' ' + str(re) + '\n')

fp.close()
