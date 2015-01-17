import gmpy
EPS = 1e-9
limit = 100

num = 1
den = 1
for i in range(10, limit):
	for j in range(i+1, limit):
		a1 = i // 10
		a2 = i % 10
		b1 = j // 10
		b2 = j % 10
		frac = float(i)/j
		num1 = 1
		den1 = 1
		if (a1 == b1 and b2 != 0):
			num1 = a2
			den1 = b2
		elif (a1 == b2 and b1 != 0):
			num1 = a2
			den1 = b1
		elif (a2 == b1 and b2 != 0):
			num1 = a1
			den1 = b2
		elif (a2 == b2 and b2 != 0):
			num1 = a1
			den1 = b1
		simple = float(num1)/den1
		if (abs(frac-simple) < EPS):
			num *= num1
			den *= den1
print(den/gmpy.gcd(num, den))