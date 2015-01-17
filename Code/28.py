ans = 1
n = 1
i = 0
step = 2
limit = 1001*1001
while n <= limit:
	n += step
	ans += n
	i += 1
	if i % 4 == 0:
		step += 2
print(ans-n)