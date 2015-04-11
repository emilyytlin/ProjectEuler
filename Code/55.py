from helper_functions import is_palindrome

def is_lychrel(n):
	for i in range(0, 50):
		n += int(str(n)[::-1])
		if is_palindrome(n):
			return False
	return True

count = 0
for i in range(1, 10000):
	if is_lychrel(i):
		count += 1
print(count)