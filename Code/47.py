def is_prime(n):
	if (n == 2 or n == 3):
		return True
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def prime_factors(n):
	i = 2
	count = 0
	while i*i <= n:
		if n % i == 0:
			count += 1
			while n % i == 0:
				n /= i
			if n != 1 and is_prime(n):
				count += 1
		i += 1
	return count

num = 647
streak = 1
while True:
	if streak == 4:
		break
	if prime_factors(num) == 4:
		streak += 1
	else:
		streak = 0
	num += 1

print(num - 4)