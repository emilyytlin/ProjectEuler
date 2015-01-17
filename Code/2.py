prev = 1
curr = 2
sum = 0
while True:
	if curr > 4000000:
		break
	if curr % 2 == 0:
		sum = sum + curr
	temp = curr
	curr = curr + prev
	prev = temp
print sum