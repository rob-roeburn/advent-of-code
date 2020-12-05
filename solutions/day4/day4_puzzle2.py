#!/usr/bin/env python
# coding: utf-8
import re


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def byr(__value):
    return (1920 <= int(__value) <= 2002)


# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def iyr(__value):
    return (2010 <= int(__value) <= 2020)


# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def eyr(__value):
    return (2020 <= int(__value) <= 2030)


# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
def hgt(__value):
    hgt_re = re.compile('[0-9]+')
    if ('cm' in __value):
        return (int(hgt_re.findall(__value)[0])
                >= 150 and int(hgt_re.findall(__value)[0]) <= 193)
    elif ('in' in __value):
        return (int(hgt_re.findall(__value)[0])
                >= 59 and int(hgt_re.findall(__value)[0]) <= 76)


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def hcl(__value):
    hcl_re = re.compile('#[0-f]{6}$')
    return (len(hcl_re.findall(__value)) > 0)


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def ecl(__value):
    return (__value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def pid(__value):
    pid_re = re.compile('[0-9]{9}$')
    return (len(pid_re.findall(__value)) > 0)


# cid (Country ID) - ignored, missing or not.
def cid(__value):
    return True


validator = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt,
             'hcl': hcl, 'ecl': ecl, 'pid': pid, 'cid': cid}


def validatePassports(values):
    passportElements = {}
    passportComplete = False
    passportValid = False
    passportCount = 0
    for value in values:
        if (value == ''):
            passportComplete = True
        else:
            for element in value.split(" "):
                passportElements[element.split(":")[0]] = element.split(":")[1]
        if (passportComplete):
            if (all(x in passportElements for x in
                    ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])):
                for key, value in passportElements.items():
                    if (validator[key](value)):
                        passportValid = True
                    else:
                        passportValid = False
                        break
                if (passportValid):
                    passportCount += 1
                passportValid = False
            passportElements = {}
            passportComplete = False
    return passportCount


values = []

with open('day4_input') as fp:
    line = fp.readline()
    while line:
        if (line != ''):
            values.append(line.strip())
        line = fp.readline()

print(validatePassports(values))
