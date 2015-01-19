coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200

table = [0]*201
table[0] = 1
for i in coins:
	for j in range(i, n+1):
		table[j] += table[j-i]
print(table[200])