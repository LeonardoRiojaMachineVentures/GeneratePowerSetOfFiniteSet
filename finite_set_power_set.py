import itertools
set
s = itertools.product([True, False], repeat = 3)
print(s)
for i in s:
	print(i)