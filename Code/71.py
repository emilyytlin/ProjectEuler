from fractions import Fraction

n = 1000000
fractions = set()
for i in range(1, n+1):
	fractions.add(Fraction(i*3//7, i))
sorted_fractions = sorted(fractions)
print(sorted_fractions[len(sorted_fractions)-2].numerator)