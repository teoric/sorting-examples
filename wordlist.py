#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

u"""Currently dysfunctional program to genereate a word frequency list.

Does not work anymore because pyuca is now python 3 only:
<https://github.com/jtauber/pyuca/issues/3>
"""

import locale
locale.setlocale(locale.LC_ALL, "")

from pyuca import Collator
import os
to_dir = os.path.dirname(os.path.realpath(__file__))
ALL_KEYS = os.path.join(to_dir, 'allkeys.txt')

# download ALL_KEYS file to directory of script
# (for older versions of pyuca)
if not os.access(ALL_KEYS, os.R_OK):
    import urllib
    urllib.urlretrieve('http://www.unicode.org/Public/UCA/latest/allkeys.txt',
        ALL_KEYS)


c = Collator(ALL_KEYS)
# available from http://www.unicode.org/Public/UCA/latest/allkeys.txt

import fileinput
import regex

diff_line = regex.compile(ur'(?V1)^(?:@@|\+{3}|\-|\s(?:\s\s)*(?=\S))')

from collections import defaultdict
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
