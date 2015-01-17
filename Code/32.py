ans_set = set()
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

for i in range(2, 99):
	start = 1234 if i <= 9 else 123
	end = 9876 if i <= 9 else 987
	for j in range(start, end+1):
		k = i*j
		num = str(k) + str(i) + str(j)
		if is_pandigital(num):
			ans_set.add(k)
print(sum(ans_set))