import gmpy

primes = [3] # 2 is irrelevant
curr = 5
def is_prime(n):
	for i in primes:
		if i * i > n:
			break
		if n % i == 0:
			return False
	return True

def conjecture(n):
	for prime in primes:
		temp = (n-prime)/2
		if gmpy.is_square(temp):
			return True
	return False

while True:
	if is_prime(curr):
		primes.append(curr)
	elif not conjecture(curr):
		break
	curr += 2
print(curr)