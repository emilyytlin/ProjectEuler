def is_palindrome(n):
	return str(n) == str(n)[::-1]

nums = "123456789"
def is_pandigital(n):
	if len(n) < 9 or len(n) > 9:
		return False
	for i in nums:
		found = False
		for j in n:
			if i == j:
				found = True
				break
		if not found:
			return False
	return True

def eratoshenes(n):
	multiples = set()
	primes = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.add(i)
			multiples.update(range(i*i, n+1, i))
	return primes

def is_prime(n):
	if (n == 2 or n == 3):
		return True
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True