from helper_functions import eratoshenes
n = 1000000
primes = sorted(eratoshenes(n))
maxl = 0
maxs = 0
for i in range(0, 4):
	s = 0
	l = 0
	currs = 0
	currl = 0
	for j in range(i, len(primes)):
		if s > n:
			break
		s += primes[j]
		l += 1
		if s in primes:
			currs = s
			currl = l
	if (currl > maxl):
		maxl = currl
		maxs = currs
print(maxs)