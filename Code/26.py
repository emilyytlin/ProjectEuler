primes = []
def is_prime(n):
	if n == 2 or n == 3:
		return True
	for i in range(2, n):
		if i * i > n:
			break
		if n % i == 0:
			return False
	return True
primes = list(x for x in range(999, 1, -1) if is_prime(x))
print(primes)
#check big primes?