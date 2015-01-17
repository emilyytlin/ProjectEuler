import itertools
a = '0123456789'
count = 1
for i in itertools.permutations(a):
	if count == 1e6:
		print(''.join(i))
		break
	else:
		count += 1