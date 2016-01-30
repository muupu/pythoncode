#-*- coding: UTF-8 -*-

from difflib_comments import SequenceMatcher, Differ
from pprint import pprint as _pprint

def test_Differ():
	text1 = '''  1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
'''.splitlines(1)
	print text1
	# print text1[0][-1]
	text2 = '''  1. Beautiful is better than ugly.
3.   Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
'''.splitlines(1)
	print text2
	# print text2[0][-1]
	d = Differ()
	result = list(d.compare(text1, text2))
	_pprint(result)

def test_Differ2():
	print ''.join(Differ().compare('one\ntwo\nthree\n'.splitlines(1),
		'ore\ntree\nemu\n'.splitlines(1))),

def test_fancy_replace():
	d = Differ()
	results = d._fancy_replace(['abcDefghiJkl\n'], 0, 1,
    							['abcdefGhijkl\n'], 0, 1)
	print ''.join(results),

def test_qformat():
	d = Differ()
	results = d._qformat('\tabcDefghiJkl\n', '\tabcdefGhijkl\n',
		'  ^ ^  ^      ', '  ^ ^  ^      ')
	for line in results: 
		print repr(line)

if __name__ == "__main__":
	# test_Differ()
	test_Differ2()
	# test_fancy_replace()
	# test_qformat()