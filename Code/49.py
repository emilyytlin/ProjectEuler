from helper_functions import eratoshenes, is_prime
import itertools
x = 3330

def prime_permutations(n):
	ans = 0
	permutations = [int(''.join(x)) for x in itertools.permutations(str(n))]
	result = []
	for p in permutations:
		if n != p and p > 1000 and is_prime(p):
			result.append(p)
	result.append(n)
	result.sort()
	for r in result:
		if r + x in result and r + x + x in result:
			ans = "{0}{1}{2}".format(r, r+x, r+x+x)
	return ans

primes = sorted(eratoshenes(10000))
for p in primes:
	if (p > 1000):
		result = prime_permutations(p)
		if result != 0 and result != "148748178147":
			print(result)
			break
