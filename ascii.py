#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -f for fielPath
# -i for strings
# -n for numbers

import sys
import getopt
import re

def readFromFile(filePath):
    result = ''
    try:
        with open(filePath,'r') as f:
            resultArr = f.readlines()
            result = ''.join(resultArr)
    except Exception as e:
        print 'filePath illegal'
        result = ''
    return result

def convert(strings,num):
    result = []
    try:
        match = re.findall(r'([a-zA-Z0-9]+)', strings, re.S)
        for item in match:
            result.append(chr(int(item,num)))
    except Exception as e:
        print e
    return result

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'f:i:n:')
    filePath = ''
    oriStrings = ''
    num = 10
    for op, value in opts:
        if op=='-f':
            filePath = value
        elif op == '-i':
            oriStrings = value
        elif op == '-n':
            num = int(value)
    if len(filePath)>0:
        oriStrings = readFromFile(filePath)
    if len(oriStrings)>0:
        convertedStr = convert(oriStrings,num)
        print ''.join(convertedStr)
    else:
        print 'stringbuffer none'
