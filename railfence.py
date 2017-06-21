#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import re

def bars(src, bar_num):
	result = ''
	if len(src)%bar_num != 0:
		num = len(src)/bar_num + 1
	else:
		num = len(src)/bar_num
	for i in range(0,num):
		for j in range(0,bar_num):
			if (i+j*num) < len(src):
				result+=src[i+j*num]
			else:
				result=result
	return result


def main():
	if len(sys.argv) == 1:
		msg = '''
The Rail-Fence Cipher Cracker.
Useage:
	railfence.py encoded-text [regexp]
	regexp: only match results will be printed
		'''
		print msg.encode()
		exit(0)
	else:
		results = []
		src = sys.argv[1]
		for i in range(2,len(src)):
			results.append(bars(src,i))
		#remove the repeated items
		results = list(set(results))
		if len(sys.argv) == 2:
			for item in results:
				print item
		else:
			regexp = sys.argv[2]
			temp = []
			for item in results:
				if re.search(sys.argv[2], item):
					temp.append(item)
			for item in temp:
				print item


if __name__ == '__main__':
	main()
