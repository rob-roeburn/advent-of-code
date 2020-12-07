#!/usr/bin/env python
# coding: utf-8


def countAnswers(__values):
    batchComplete = False
    matrixList = []
    answerCount = {}
    answerDict = {}
    totalAnswers = 0
    personCount = 0
    for answers in __values:
        if answers == '':
            batchComplete = True
        else:
            personCount += 1
            answerDict[personCount] = (answers.split())
        if batchComplete:
            matrixList.append(answerDict)
            answerDict = {}
            personCount = 0
            batchComplete = False
    answerDict[personCount] = (answers.split())
    matrixList.append(answerDict)
    for matrix in matrixList:
        answerCount = {}
        for person in matrix.items():
            for letter in list(person)[1][0]:
                if letter in answerCount:
                    answerCount[letter] += 1
                else:
                    answerCount[letter] = 1
        for key, answer in answerCount.items():
            if (answer == len(matrix)):
                totalAnswers += 1
    return totalAnswers


values = []

with open('day6_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

print(countAnswers(values))
