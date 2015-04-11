max_sum = 0
for i in range(2, 100):
	for j in range(2, 100):
		curr_sum = 0
		power_string = str(i**j)
		for k in power_string:
			curr_sum += int(k)
		max_sum = max(max_sum, curr_sum)
print(max_sum)