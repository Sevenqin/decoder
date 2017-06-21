#!/usr/bin/env python
# -*- coding: utf-8 -*-

import modules.brainfuckModule.brainfuck as brainfuck
import sys
import getopt

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

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'f:i:')
    filePath = ''
    oriStrings = ''
    num = 10
    for op, value in opts:
        if op=='-f':
            filePath = value
        elif op == '-i':
            oriStrings = value
    if len(filePath)>0:
        oriStrings = readFromFile(filePath)
    if len(oriStrings)>0:
        brainfuck.evaluate(oriStrings)
    else:
        print 'stringbuffer none'
