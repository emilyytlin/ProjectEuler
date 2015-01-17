import itertools as it
def eratoshenes(n):
	multiples = set()
	primes = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.add(i)
			multiples.update(range(i*i, n+1, i))
	return primes

def is_Circular(n):
	l = len(n)
	for i in range(1, l):
		n = n[1:l] + n[0]
		if not (int(n) in primes):
			return False
	return True

ans = 0
limit = 1000000
primes = eratoshenes(limit)
for i in primes:
	if is_Circular(str(i)):
		ans += 1
print(ans)