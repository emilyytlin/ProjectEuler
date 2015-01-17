limit = 10000 #must be at most 4 digit number

nums = "123456789"
def is_pandigital(n):
	if len(n) < 9 or len(n) > 9:
		return False
	for i in nums:
		found = False
		for j in n:
			if i == j:
				found = True
				break
		if not found:
			return False
	return True

largest = 0
limit2 = [10, 5, 4, 3]
for i in range(1, limit):
	num = i
	limit2 = 10 if i < 10 else 5 if i < 100 else 4 if i < 1000 else 3
	for j in range(2, limit2):
		n = str(num)
		num *= j
		n += str(num)
		if is_pandigital(n) and n > largest:
			largest = n
			break
print(largest)