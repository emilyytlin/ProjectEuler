total_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 6
sundays = 0

for year in range(1901, 2001):
	total_days[1] = 29 if year % 4 == 0 else 28
	for month in range(0, 12):
		prev = total_days[11] if range == 0 else total_days[month-1]
		day = (prev + day) % 7
		if day == 0:
			sundays += 1
print(sundays)