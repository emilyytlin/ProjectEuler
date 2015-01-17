#similar to 18, 67
LENGTH = 80
FILE = '81.txt'

matrix = [[0]*(LENGTH) for x in range(LENGTH)]
with open(FILE, 'r') as f:
	i = 0
	for line in f:
		j = 0
		for word in line.split(","):
			matrix[i][j] = int(word)
			j += 1
		i += 1

for i in range(1, LENGTH):
	matrix[0][i] += matrix[0][i-1]
	matrix[i][0] += matrix[i-1][0]

for i in range(1, LENGTH):
	for j in range(1, LENGTH):
		left = matrix[i][j-1]
		up = matrix[i-1][j]
		matrix[i][j] += min(left, up)

print(matrix[LENGTH-1][LENGTH-1])