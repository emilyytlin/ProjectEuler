import gmpy

limit = 50000
ans = 0
for i in range(10, limit):
	temp = 0
	if i == sum([gmpy.fac(int(x)) for x in str(i)]):
		ans += i
print(ans)