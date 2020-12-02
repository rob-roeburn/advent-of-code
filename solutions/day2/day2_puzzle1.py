#!/usr/bin/env python
# coding: utf-8


def findValidPasswords(values):
    count = 1
    for elements in values:
        if (
            (int(elements[0].split("-")[0]) <=
                len(([pos for pos, char in enumerate(elements[2])
                    if char == elements[1].split(":")[0]])))
            and
            (int(elements[0].split("-")[1]) >=
                len(([pos for pos, char in enumerate(elements[2])
                    if char == elements[1].split(":")[0]])))
        ):
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
