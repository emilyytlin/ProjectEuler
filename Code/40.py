s = ""
n = 1
limit = 1000000
while len(s) < limit:
	s += str(n)
	n += 1
ans = 1
for i in range(7):
	ans *= int(s[10**i-1])
print(ans)