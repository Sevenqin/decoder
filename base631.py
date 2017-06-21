#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this code will deocode as far as it can be decoded by base64,32,16

import base64
import sys
import getopt

func_result = [
    lambda x:base64.b16decode(x),
    lambda x:base64.b32decode(x),
    lambda x:base64.b64decode(x)
]
def decodeSuccess(result):
    if(len(result)==0):
        return 0
    for i in result:
        if ord(i)<32 or ord(i)>127:
            return 0
    return 1

def decodeOneStep(x):
    result = ''
    canDecode = 0
    for value in func_result:
        try:
            # print value
            result = value(x)
            # print result
            if decodeSuccess(result=result):
                print 'step: '+result
                return result, 1
            else:
                continue
        except Exception as e:
            continue

    return x,0



if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'f:i:')
    filePath = ''
    oriStrings = ''
    for op, value in opts:
        if op=='-f':
            filePath = value
        elif op == '-i':
            oriStrings = value

    result = []
    if len(filePath)>0:
        try:
            with open(filePath,'r') as f:
                for line in f.readlines():
                    line = line.strip().strip('\n')
                    result.append(line)
            oriStrings = ''.join(result)
        except Exception as e:
            print e
            oriStrings = ''
    oriStrings.strip('').strip('\n')
    # print codes
    canDecode = 1
    codes = oriStrings
    while canDecode:
        codes,canDecode = decodeOneStep(codes)
        # print codes
    print 'result:'+codes
