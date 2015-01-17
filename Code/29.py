limit = 101
nums = set(int(a**b) for a in range(2, limit) for b in range(2, limit))
print(len(nums))