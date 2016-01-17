#-*- coding: UTF-8 -*-

import difflib

### find_longest_match ###
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
lm = s.find_longest_match(0, 5, 0, 9)
print lm
# Out[3]: Match(a=0, b=4, size=5)

### isjunk is defined ###
s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
lm = s.find_longest_match(0, 5, 0, 9)
print lm