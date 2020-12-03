#!/usr/bin/env python
# coding: utf-8


def findTrees(values, tree):
    trees = 0
    swerve = 0
    itervalues = iter(values)
    next(itervalues)
    for element in itervalues:
        swerve += 3
        if (swerve >= len(element)):
            swerve = swerve - len(element)
        if (element[swerve] == tree):
            trees += 1
    print(trees)
    return


values = []

with open('day3_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

findTrees(values, '#')
