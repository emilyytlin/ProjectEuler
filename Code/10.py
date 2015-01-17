primes = []
sum = 0
def is_prime(n):
	if n == 2 or n == 3:
		return True
	for i in primes:
		if i * i > n:
			break
		if n % i == 0:
			return False
	return True
for i in range(2, 2000000):
	if (is_prime(i)):
		primes.append(i)
		sum += i
print sum