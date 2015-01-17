def is_abundant(n):
	i = 1
	ans = 0
	while i*i < n:
		if n % i == 0:
			ans += (i + int(n/i))
		i += 1
	if i*i == n:
		ans += i
	return ans-n > n
limit = 20161
abundants = list(x for x in range(1, limit+1) if is_abundant(x))

sums = 0
abundant_sums = set()
for i in abundants:
	for j in abundants:
		if j >= i and i+j <= limit:
			abundant_sums.add(i+j)
print(limit*(limit+1)/2 - sum(abundant_sums))