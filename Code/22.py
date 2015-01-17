import re
with open('22.txt', 'r') as f:
	names = re.split('[^A-Z]', f.readlines()[0])
	names.sort()
	order = 1
	ans = 0
	for name in names:
		if name:
			value = 0
			for c in name:
				value += (ord(c)-64)
			ans += (value * order)
			order += 1
	print(ans)