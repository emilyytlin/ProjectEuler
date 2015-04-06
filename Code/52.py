def has_digits(x, y):
	for c in y:
		if c not in x:
			return False
	return True

n = 99
while True:
	s = str(n)
	stop = True
	for i in range(2, 7):
		if not has_digits(s, str(i * n)):
			stop = False
	if stop:
		print(n)
		break
	n += 1