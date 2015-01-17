import math
eps = 1e-9

def factors(n):
	count = 0
	lim = math.sqrt(n)
	for i in range(1, int(lim)+1):
		if n % i == 0:
			count += 1
	count *= 2
	if abs(lim - int(lim)) < eps:
		count -= 1
	return count
i = 1
sum = 1
while True:
	if (factors(sum) > 500):
		break
	i += 1
	sum += i
print(sum)