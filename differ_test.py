#-*- coding: UTF-8 -*-

from difflib_comments import SequenceMatcher, Differ

def test_Differ():
	text1 = '''  1. Beautiful is better than ugly.
			2. Explicit is better than implicit.
			3. Simple is better than complex.
			4. Complex is better than complicated.
			'''.splitlines(1)
	print len(text1)
	print text1[0][-1]
	text2 = '''  1. Beautiful is better than ugly.
			3.   Simple is better than complex.
			4. Complicated is better than complex.
			5. Flat is better than nested.
			'''.splitlines(1)
	print len(text2)
	print text2[0][-1]


if __name__ == "__main__":
