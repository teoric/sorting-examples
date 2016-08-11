#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

u"""Program to genereate a sorted word frequency list."""

from collections import defaultdict
import fileinput
import locale
import os
import regex
import sys
from pyuca import Collator

reload(sys)
sys.setdefaultencoding("utf-8")

locale.setlocale(locale.LC_ALL, "")

c = Collator()

diff_line = regex.compile(ur'(?V1)^(?:@@|\+{3}|\-|\s(?:\s\s)*(?=\S))')

words = defaultdict(int)

for line in fileinput.input(openhook=fileinput.hook_encoded("UTF-8")):
    if diff_line.match(line):
        continue
    line = unicode(line.strip()).lower()
    for m in regex.finditer(ur'(?V1)#?(?:\w|-)*\p{L}{2,}(?:\w|-)*', line):
        w = unicode(m.group(0))
        if w[0] == "#":
            continue
        if w[0] == "#":
            continue
        words[w] += 1

for w in sorted(words.keys(), key=c.sort_key):
    print(u"{:4d} {}".format(words[w], w).encode("UTF-8"))
