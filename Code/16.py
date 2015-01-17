big = 2**1000
ans = 0
while big > 0:
	ans += big % 10
	big //= 10
print(ans)