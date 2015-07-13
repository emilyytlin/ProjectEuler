import gmpy
import math
def increment(n):
	i = 1000 * (n % 10)
	n //= 10
	scale = 100000
	while n > 0:
		digit = n % 10
		i += digit * scale
		n //= 10
		scale *= 100
	return i

base = 1020304050607080900
num = base
i = 0
while num < 1929394959697989900:
	if(gmpy.is_square(num)):
		break
	i += 1
	num = base + increment(i)
print(math.sqrt(num))