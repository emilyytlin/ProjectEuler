def eratoshenes(n):
	multiples = set()
	primes = set()
	for i in range(2, n+1):
		if i not in multiples:
			primes.add(i)
			multiples.update(range(i*i, n+1, i))
	return primes

def is_trunc(n):
	if (n <= 7):
		return False
	s = str(n)
	for j in range(1, len(s)):
		if int(s[0:j]) not in primes:
			return False
	for j in range(1, len(s)):
		if int(s[j:len(s)]) not in primes:
			return False
	return True

primes = eratoshenes(1000000)
count = 0
ans = 0
for i in primes:
	if is_trunc(i):
		count += 1
		ans += i
		print("{}: {}".format(count, i))

print(ans)