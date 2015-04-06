import math
h = 144
while True:
	H = h*(2*h-1)
	T = (1 + math.sqrt(1 + 8*H))/2
	P = (1 + math.sqrt(1 + 24*H))/6
	if (T.is_integer() and P.is_integer()):
		print(H)
		break
	h += 1