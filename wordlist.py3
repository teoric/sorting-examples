#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""program to generate a sorted word frequency list."""
import locale

import fileinput
import regex
from pyuca import Collator


locale.setlocale(locale.LC_ALL, "")

# import os
# download ALL_KEYS file to directory of script
# available from http://www.unicode.org/Public/UCA/latest/allkeys.txt
# now included in pyuca
# if not os.access(ALL_KEYS, os.R_OK):
#     import urllib
#     urllib.request.urlretrieve(
#         'http://www.unicode.org/Public/UCA/latest/allkeys.txt',
#         ALL_KEYS)
# to_dir = os.path.dirname(os.path.realpath(__file__))
# ALL_KEYS = os.path.join(to_dir, 'allkeys.txt')
# c = Collator(ALL_KEYS)

c = Collator()


diff_line = regex.compile(r'(?V1)^(?:[+]{3}|-|@@|\s(?:\s\s)*(?=\S))')

from collections import defaultdict
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

for w in sorted(words.keys(), key=c.sort_key):
    print(r"{:4d} {}".format(words[w], w))
