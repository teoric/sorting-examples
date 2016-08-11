#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""program to genereate a word frequency list. Sorting with strxfrm.

Does not sort correctly on Mac."""
import locale

from collections import defaultdict
import fileinput
import regex

locale.setlocale(locale.LC_ALL, "")
diff_line = regex.compile(r'(?V1)^(?:[+]{3}|-|@@|\s(?:\s\s)*(?=\S))')


words = defaultdict(int)

for line in fileinput.input(openhook=fileinput.hook_encoded("UTF-8")):
    if diff_line.match(line):
        continue
    line = line.strip().lower()
    for m in regex.finditer(r'(?V1)#?(\w|-)*\p{L}{2,}(\w|-)*', line):
        w = m.group(0)
        if w[0] == "#":
            continue
        words[w] += 1

for w in sorted(words.keys(), key=locale.strxfrm):
    print(r"{:4d} {}".format(words[w], w))
