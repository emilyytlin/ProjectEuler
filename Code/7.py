primes = []
count = 0
curr = 2
def is_prime(n):
	if n == 2 or n == 3:
		return True
	for i in primes:
		if i * i > n:
			break
		if n % i == 0:
			return False
	return True
while True:
	if (is_prime(curr)):
		primes.append(curr)
		count += 1
	if count == 10001:
		break
	curr = curr + 1
print curr