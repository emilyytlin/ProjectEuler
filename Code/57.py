a = 3
b = 2
count = 0
for i in range(0, 1000):
	tempa = a
	tempb = b
	a = tempa + tempb*2
	b = tempa + tempb
	if (len(str(a)) > len(str(b))):
		count += 1
print(count)