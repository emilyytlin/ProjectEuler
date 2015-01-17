big = 1
ans = 0
for i in range(2, 101):
	big *= i
while big > 0:
	ans += big % 10
	big //= 10
print(ans)