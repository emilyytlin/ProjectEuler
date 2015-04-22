from helper_functions import is_prime

diagonals = 5
primes = 3
length = 3
curr = 9
while primes/diagonals >= .1:
	diagonals += 4
	length += 2
	for i in range(0, 4):
		curr += (length-1)
		if is_prime(curr):
			primes += 1
print(length)
