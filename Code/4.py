max = 0
ans = 0
def is_palindrome(n):
	return str(n) == str(n)[::-1]
for i in range(999, 101, -1):
	for j in range(999, 101, -1):
		curr = i*j
		if is_palindrome(curr) and curr > max:
			ans = curr
			max = curr
print ans