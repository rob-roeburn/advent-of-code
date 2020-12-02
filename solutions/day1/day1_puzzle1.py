#!/usr/bin/env python
# coding: utf-8


def findSum(values, sum):
    for sum1 in values:
        for sum2 in values:
            if((sum1 + sum2) == sum):
                print(
                    sum1,
                    sum2,
                    sum1 + sum2,
                    sum1 * sum2
                )
                return


values = []

with open('day1_input') as fp:
    line = int(fp.readline())
    while line:
        if(line != ''):
            values.append(int(line))
        line = fp.readline()

findSum(values, 2020)
