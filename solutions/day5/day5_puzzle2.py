#!/usr/bin/env python
# coding: utf-8


def tophalf(__values):
    __values = range(__values[0], __values[0]+int(len(__values)/2))
    if (len(__values) == 1):
        return __values[0]
    return __values


def bottomhalf(__values):
    __values = range(int(__values[0] + (((__values[len(__values) - 1] + 1) -
                     __values[0]) / 2)), __values[len(__values) - 1] + 1)
    if (len(__values) == 1):
        return __values[0]
    return __values


def findPasses(__values, mult, seats, seatrow):
    for value in __values:
        for element in value:
            if (element == 'F'):
                seats = tophalf(seats)
            if (element == 'B'):
                seats = bottomhalf(seats)
            if (element == 'L'):
                seatrow = tophalf(seatrow)
            if (element == 'R'):
                seatrow = bottomhalf(seatrow)
    return seats * mult + seatrow


def findGap(__values):
    sortedpasses = sorted(__values)
    for key, currpass in enumerate(sortedpasses):
        if (key <= len(sortedpasses)):
            if ((sortedpasses[key+1] - currpass) != 1):
                return currpass+1
    return


values = []
passes = []

with open('day5_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

for seat in values:
    seatID = findPasses(seat, 8, range(0, 128), range(0, 8))
    passes.append(seatID)

print(findGap(passes))
