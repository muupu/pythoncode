#-*- coding: UTF-8 -*-

import difflib

### find_longest_match ###
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
lm = s.find_longest_match(0, 5, 0, 9)
print lm
