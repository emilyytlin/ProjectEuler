import itertools as it

divisors = [0, 2, 3, 5, 7, 11, 13, 17]
permutations = it.permutations("0123456789")
ans = 0

for p in permutations:
	is_pandigital = True
	for i in range(1, 8):
		num = int(str(p[i]) + str(p[i+1]) + str(p[i+2]))
		if num % divisors[i] != 0:
			is_pandigital = False
			break
	if is_pandigital:
		s = ""
		for i in p:
			s = str(s) + str(i)
		s = int(s)
		ans += s
print(ans)