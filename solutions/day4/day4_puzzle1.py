#!/usr/bin/env python
# coding: utf-8


def validatePassports(values):
    passportElements = []
    passportComplete = False
    passportCount = 0
    for value in values:
        if(value == ''):
            passportComplete = True
        else:
            for element in value.split(" "):
                passportElements.append(element.split(":")[0])
        if (passportComplete):
            if(all(x in passportElements for x in
                   ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])):
                passportCount += 1
            passportElements = []
            passportComplete = False
    return passportCount


values = []

with open('day4_input') as fp:
    line = fp.readline()
    while line:
        if(line != ''):
            values.append(line.strip())
        line = fp.readline()

print(validatePassports(values))
