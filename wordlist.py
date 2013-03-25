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

for line in fileinput.input(openhook=fileinput.hook_encoded("UTF-8")):
    line = unicode(line.strip()).lower()
    if diff_line.match(line) or del_line.match(line):
        continue
    line = regex.sub(ur'^-', "", line)
    for m in regex.finditer(ur'#?(?:\w|-)*\p{L}{2,}(?:\w|-)*', line):
        w = m.group(0)
        if w[0] == "#":
            continue
        if w[0] == "#":
            continue
        words[w] += 1

for w in sorted(words.keys(), key=c.sort_key):
    print(u"{:4d} {}".format(words[w], w).encode("UTF-8"))

