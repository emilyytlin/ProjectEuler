import re

triangles = set()
words = []
for n in range(1, 30):
	triangles.add(n*(n+1)//2)
with open('42.txt', 'r') as f:
	words = re.split('[^A-Z]+', f.readlines()[0])

ans = 0
for word in words:
	val = 0
	for c in word:
		val += (ord(c)-64)
	if val in triangles:
		ans += 1
print(ans)