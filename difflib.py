#-*- coding: UTF-8 -*-

import difflib

### find_longest_match ###
s = SequenceMatcher(None, " abcd", "abcd abcd")
s.find_longest_match(0, 5, 0, 9)
