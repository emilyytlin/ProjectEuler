EPS = 1e-9
limit = 15499.0/94744

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def denom():
	num = 1
	den = 1
	for p in primes:
		num *= p-1
		den *= p
		for i in range(2, p):
			if num*i / (den*i-1.0) < limit:
				return(den*i)
	return "need more priems"
print(denom())