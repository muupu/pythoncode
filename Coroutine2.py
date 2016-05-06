
def consumer():
	while True:
		line = yield
		print(line.upper())

def producter():
	with open('D:\\Python32\\1.py', 'r') as f:
		for i, line in enumerate(f):
			yield line
			print('processed line %d' % i)

c = consumer()
next(c)
for line in producter():
	c.send(line)

