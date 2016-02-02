#-*- coding: UTF-8 -*-

from difflib_comments import SequenceMatcher, get_close_matches

def test_find_longest_match():
	### find_longest_match ###
	s = SequenceMatcher(None, " abcd", "abcd abcd")
	lm = s.find_longest_match(0, 5, 0, 9)
	print lm
	# Out[3]: Match(a=0, b=4, size=5)

	### isjunk is defined ###
	s = SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
	lm = s.find_longest_match(0, 5, 0, 9)
	print lm
	# Match(a=1, b=0, size=4)

	### no blocks match ###
	s = SequenceMatcher(None, "ab", "c")
	lm = s.find_longest_match(0, 2, 0, 1)
	print lm
	# Match(a=0, b=0, size=0)

	### stripping common prefix or suffix ###
	s = SequenceMatcher(None, "ab", "acab")
	lm = s.find_longest_match(0, 2, 0, 4)
	print lm
	# Match(a=0, b=0, size=1)

def test_find_longest_match2():
	### find_longest_match ###
	s = SequenceMatcher(None, "abcdeabce", "abcecabd")
	lm = s.find_longest_match(0, 9, 0, 8)
	print lm
	# Out[3]: Match(a=5, b=0, size=4)

def test_get_matching_blocks():
	s = SequenceMatcher(None, "abxcd", "abcd")
	mb = s.get_matching_blocks()
	print mb

def test_get_opcodes():
	a = "qabxcd"
	b = "abycdf"
	s = SequenceMatcher(None, a, b)
	for tag, i1, i2, j1, j2 in s.get_opcodes():
		print ("%7s a[%d:%d] (%s) b[%d:%d] (%s)" % (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))

def test_get_grouped_opcodes():
	from pprint import pprint
	a = map(str, range(1,40))
	b = a[:]
	b[8:8] = ['i']     # Make an insertion
	b[20] += 'x'       # Make a replacement
	b[23:28] = []      # Make a deletion
	b[30] += 'y'       # Make another replacement
	pprint(list(SequenceMatcher(None,a,b).get_grouped_opcodes()))

def test_getCloseMatches():
	cm = get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
	print cm

if __name__ == "__main__":
    # test_find_longest_match()
    # test_find_longest_match2()
    # test_get_matching_blocks()
    # test_get_opcodes()
    # test_get_grouped_opcodes()
    test_getCloseMatches()