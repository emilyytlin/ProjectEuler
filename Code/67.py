#same as 18
LENGTH = 100
FILE = '67.txt'

matrix = [[0]*(i+1) for i in range(LENGTH)]
with open(FILE, 'r') as f:
	i = 0
	for line in f:
		j = 0
		for word in line.split():
			matrix[i][j] = int(word)
			j += 1
		i += 1
for i in range(1, LENGTH):
	for j in range(len(matrix[i])):
		left = 0 if j == 0 else matrix[i-1][j-1]
		right = 0 if j == len(matrix[i])-1 else matrix[i-1][j]
		matrix[i][j] += max(left, right)

ans = 0
for i in range(LENGTH):
	ans = max(ans, matrix[LENGTH-1][i])
print(ans)