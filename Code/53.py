import gmpy 
c = 0
for n in range(23, 101):
	for r in range(2, n):
		if gmpy.comb(n, r) > 1000000:
			c += 1
print(c)