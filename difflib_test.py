#-*- coding: UTF-8 -*-

import difflib

### find_longest_match ###
s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
lm = s.find_longest_match(0, 5, 0, 9)
print lm
# Out[3]: Match(a=0, b=4, size=5)

### isjunk is defined ###
s = difflib.SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
lm = s.find_longest_match(0, 5, 0, 9)
print lm
# Match(a=1, b=0, size=4)

### no blocks match ###
s = difflib.SequenceMatcher(None, "ab", "c")
lm = s.find_longest_match(0, 2, 0, 1)
print lm