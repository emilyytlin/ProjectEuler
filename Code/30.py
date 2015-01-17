limit = 200000
ans = 0
for i in range(2, limit):
	if i == sum([int(x)**5 for x in str(i)]):
		ans += i
print(ans)