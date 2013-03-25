#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
locale.setlocale(locale.LC_ALL, "")

from pyuca import Collator
c = Collator("allkeys.txt")
# available from http://www.unicode.org/Public/UCA/latest/allkeys.txt

words = [u"Ärger", u"arg", u"Abel", u"Käse", "Kaese", "Kasein", u"Zeichen"]

words.sort(key=c.sort_key)
print(words)
