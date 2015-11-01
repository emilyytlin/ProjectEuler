import math

with open('99.txt', 'r') as f:
	largest = 0
	largest_line = 1
	line = 1
	for row in f:
		nums = row.split(',')
		curr = int(nums[1])*math.log(int(nums[0]))
		if (curr > largest):
			largest = curr
			largest_line = line
		line += 1
print(largest_line)