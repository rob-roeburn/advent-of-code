#!/usr/bin/env python
# coding: utf-8


def findTrees(values, tree, swerverate, skip):
    trees = 0
    swerve = 0
    i = 0
    i += skip
    while i < len(values):
        swerve += swerverate
        if (swerve >= len(values[i])):
            swerve = swerve - len(values[i])
        if (values[i][swerve] == tree):
            trees += 1
        i += skip
    return trees


values = []

with open('day3_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

print(
    findTrees(values, '#', 1, 1) *
    findTrees(values, '#', 3, 1) *
    findTrees(values, '#', 5, 1) *
    findTrees(values, '#', 7, 1) *
    findTreesA(values, '#', 1, 2)
)
