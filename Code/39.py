pmax = 0
solmax = 0

for i in range(12, 1001):
	currmax = 0
	c_min = i//3 + 1 if i % 3 == 0 else i//3
	c_max = i//2 + 1 if i % 2 == 0 else i//2
	for c in range(c_min, c_max+1):
		a_max = (i-c)//2
		for a in range(1, a_max+1):
			b = i-c-a
			if a*a + b*b == c*c:
				currmax += 1
	if currmax > solmax:
		solmax = currmax
		pmax = i
print(pmax)