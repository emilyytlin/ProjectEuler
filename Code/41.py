import itertools

def eratoshenes(n):
	multiples = set()
	primes = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.add(i)
			multiples.update(range(i*i, n+1, i))
	return primes
primes = eratoshenes(31427) #sqrt(987654321)

def is_prime(n):
	for prime in primes:
		if n % prime == 0:
			return False
	return True

done = False
for i in range(10, 3, -1):
	s = ''.join(str(x) for x in range(1, i))
	permutations = [int(''.join(x)) for x in itertools.permutations(s)]
	for i in range(len(permutations)-1, 0, -1):
		if is_prime(permutations[i]):
			print(permutations[i])
			done = True
			break
	if done:
		break