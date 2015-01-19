def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n <= 0:
		return False
	for i in range(2, n):
		if i * i > n:
			break
		if n % i == 0:
			return False
	return True

ans = 0
max_sequence = 0
for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		n = 0
		while is_prime(n*n + a*n + b):
			if n > max_sequence:
				max_sequence = n
				ans = a*b
			n += 1
print(ans)