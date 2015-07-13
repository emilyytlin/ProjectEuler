def end89(n):
	while n != 1 and n != 89:
		count = 0
		while n > 0:
			digit = n % 10
			count += (digit * digit)
			n //= 10
		n = count
	return n == 89

ans = 0
for i in range(2, 10000001):
	if (end89(i)):
		ans += 1
print(ans)