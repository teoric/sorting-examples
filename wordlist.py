#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
locale.setlocale(locale.LC_ALL, "")

from pyuca import Collator
c = Collator("allkeys.txt")
# available from http://www.unicode.org/Public/UCA/latest/allkeys.txt

import fileinput
import regex

diff_line = regex.compile(ur'^(?:[+-]{3}|@@)')
del_line = regex.compile(ur'^-')

from collections import defaultdict
words = defaultdict(int)

for line in fileinput.input():
    line = unicode(line.strip()).lower()
    if diff_line.match(line) or del_line.match(line):
        continue
    for w in regex.split(ur'\W+',line):
        words[w] += 1

for w in sorted(words.keys(),key=c.sort_key):
    print(u"{:4d} {}".format(words[w], w))

