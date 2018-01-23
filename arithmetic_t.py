

from timeit import Timer
# List事件的时间复杂度

def list_append():
	li = []
	for i in range(0,10000):
		li.append(i)


def list_add():
	li = []
	for i in range(0,10000):
		li = li + [i] # li = li + [i] 与 li += [i] 不相同


def list_producter():
	li = [i for i in range(0,10000)]


def list_range():
	li = list(range(0,10000))

def list_extend():
	li = []
	for i in range(0,10000):
		li.extend([i])

def list_instert():
	li = []
	for i in range(0,10000):
		li.insert(-1,i)


names = [
# "list_append",
#'list_add',
# 'list_producter',
# 'list_range',
'list_extend',
'list_instert']


for i in names:
	timer = Timer(('%s()' % i),('from __main__ import %s' % i))
	print("%s :" % i ,timer.timeit(1000))


