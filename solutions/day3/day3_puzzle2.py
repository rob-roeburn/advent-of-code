#!/usr/bin/env python
# coding: utf-8


def findValidPasswords(values, tree, swerverate, skip):
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
    findValidPasswords(values, '#', 1, 1) *
    findValidPasswords(values, '#', 3, 1) *
    findValidPasswords(values, '#', 5, 1) *
    findValidPasswords(values, '#', 7, 1) *
    findValidPasswords(values, '#', 1, 2)
)
