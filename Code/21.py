def d(n):
	i = 1
	ans = 0
	while i*i < n:
		if n % i == 0:
			ans += (i + int(n/i))
		i += 1
	if i*i == n:
		ans += i
	return ans-n

ans = 0
for a in range(10000):
	b = d(a)
	if a != b and d(b) == a:
		ans += (a+b)
print(ans//2)