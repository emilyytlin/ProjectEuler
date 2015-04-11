import math
pentagons = [int(x*(3*x-1)/2) for x in range(1, 5000)]

def is_pentagon(n):
	num = (1 + math.sqrt(1 + 24*n))/6
	return num.is_integer()

for i in range(0, 4999):
	for j in range(i+1, 4999):
		if is_pentagon(pentagons[j] - pentagons[i]) and is_pentagon(pentagons[j] + pentagons[i]):
			print(pentagons[j]-pentagons[i])
