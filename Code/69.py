from helper_functions import eratoshenes
n = 1
i = 0
primes = sorted(eratoshenes(1000))
while n*primes[i] < 1000000:
	n *= primes[i]
	i += 1
print(n)