#!/usr/bin/env python
# coding: utf-8


def findValidPasswords(values):
    count = 1
    for elements in values:
        subcount = 0
        if (
            elements[1].split(":")[0] ==
            elements[2][int(elements[0].split("-")[0])-1]
        ):
            subcount += 1
        if (
            elements[1].split(":")[0] ==
            elements[2][int(elements[0].split("-")[1])-1]
        ):
            subcount += 1
        if (subcount == 1):
            count += 1
    print(count)
    return


values = []

with open('day2_input') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        if(line != ''):
            line = line.strip().split(" ")
            values.append(line)

findValidPasswords(values)
