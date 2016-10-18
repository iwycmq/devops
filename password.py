#!/usr/bin/env python
#coding:utf-8

#create a random password

import string
from random import choice, shuffle

low_lst = [_ for _ in string.lowercase if _ not in 'lo']
upp_lst = [_ for _ in string.uppercase if _ not in 'IO']
dig_lst = [_ for _ in string.digits if _ not in '10']
pun_lst = [_ for _ in string.punctuation if _ not in r'\'"`~|^@,.{[()]}:;']

def six():
    password = map(choice, [upp_lst, dig_lst, pun_lst, low_lst, low_lst, low_lst])
    shuffle(password)
    return ''.join(password)

def eight():
    password = map(choice, [upp_lst, dig_lst, pun_lst, low_lst, low_lst, low_lst, low_lst, low_lst])
    shuffle(password)
    return ''.join(password)

