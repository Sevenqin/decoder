#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt
import modules.brainfuckModule.brainfuck as brainfuck

ENCODE = {
    '.?':'>',   '?.':'<',
    '..':'+',   '!!':'-',
    '!.':'.',   '.!':',',
    '!?':'[',   '?!':']'
}
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


def convert(oriStrings):
    res = [x for x in oriStrings if x=='!' or x=='.' or x=='?']
    resStr = ''.join(res)
    brainfuckArr = []
    for i in range(0,len(resStr),2):
        # print resStr[i:i+2]
        val = ENCODE.get(resStr[i:i+2], None)
        if val:
            brainfuckArr.append(val)
        else:
            print 'convertwith illegal charter'
            break
    brainfuckStr = ''.join(brainfuckArr)
    print brainfuckStr
    brainfuck.evaluate(brainfuckStr)
    # print brainfuckStr



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
        convert(oriStrings)
    else:
        print 'stringbuffer none'
