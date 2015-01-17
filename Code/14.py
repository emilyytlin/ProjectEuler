m = 0
ans = 0
def chain(n):
	count = 1
	while n != 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		count += 1
	return count
for i in range(999999, 1, -1):
	curr = chain(i)
	if curr > m:
		m = curr
		ans = i
print(ans)