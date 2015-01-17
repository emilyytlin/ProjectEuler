ans = 0
for i in range(1, 1001):
	ans += pow(i, i, 10000000000)
print(ans % 1e10)