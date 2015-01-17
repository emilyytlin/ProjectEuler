def is_palindrome(n):
	return str(n) == str(n)[::-1]

limit = 1000001
ans = 0
for i in range(1, limit):
	if is_palindrome(i) and is_palindrome("{0:b}".format(i)):
		ans += i
print(ans)