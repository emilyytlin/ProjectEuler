a = 0
b = 0
for i in range(1, 101):
	a = a + i * i
for i in range(1, 101):
	b = b + i
b = b * b
print(b - a)