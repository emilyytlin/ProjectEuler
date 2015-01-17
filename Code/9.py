import math
for c in range(500, 413, -1):
	temp = 1.0*1000-c
	b = -1
	a = -1
	num = -temp*temp+2*c*c
	if num > 0:
		b = math.sqrt(num)/2+temp/2
		a = 1000 - b - c
	print ("c = {}, b = {}, a = {}".format(c, b, a))