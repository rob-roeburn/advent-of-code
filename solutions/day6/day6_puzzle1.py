#!/usr/bin/env python
# coding: utf-8


def countAnswers(__values):
    batchComplete = False
    answerCount = 0
    answerDict = {}
    for answers in __values:
        for answer in answers:
            answerDict[answer] = 1
        if answers == '':
            batchComplete = True
        if batchComplete:
            answerCount += len(answerDict)
            answerDict = {}
            batchComplete = False
    answerCount += len(answerDict)
    return answerCount


values = []

with open('day6_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

print(countAnswers(values))
