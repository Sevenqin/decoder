#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

__author__  = 'zhangxf55'
__date__    = '2017-05-02'
__version__ = '1.1.0'

ENCODE = {
    # Alphabet
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    # Digitals
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    # Interpunction
    ',': '--..--', '.': '.-.-.-',  ':': '---...',  ';': '-.-.-.',
    '?': '..--..', '=': '-...-',   "'": '.----.',  '/': '-..-.',
    '!': '-.-.--', '-': '-....-',  '_': '..--.-',  '(': '-.--.',
    ')': '-.--.-', '$': '...-..-', '&': '....',    '@': '.--.-.'

    # Addon
}

DECODE = dict(map(lambda t:(t[1],t[0]),ENCODE.items()))


def encode(msg):
    message = ''
    for c in msg:
        if c == ' ':
            message += ' '
        else:
            message += ENCODE[c.upper()] + ' '
    return message


def decode(morseCode):
    #print morseCode
    message = ''
    list = morseCode.split(' ')
    for s in list:
        message += DECODE[s]
    return message


def main():
	if len(sys.argv) < 3:
		msg = '''
		morse decoder and encoder, useage:
		morse.py -d/-e string
		e.g. morse code should be quoted by ""
		'''
		print msg
		exit(0)
	else:
		if sys.argv[1] == '-d':
			print decode(sys.argv[2])
		elif sys.argv[1] == '-e':
			print encode(sys.argv[2])
		else:
			print 'unsupport method: ' + sys.argv[2]
			exit(0)


if __name__ == '__main__':
	main()
