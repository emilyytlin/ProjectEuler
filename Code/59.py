import collections

def analyze(cipher, index, key_length):
	count = 0
	sample = []
	for char in cipher:
		if count % key_length == index:
			sample.append(char)
		count += 1
	counter = collections.Counter(sample).most_common(5)
	# print(counter)
	for freq in counter:
		key = int(freq[0]) ^ ord(' ')
		if (key <= ord('z') and key >= ord('a')):
			# print("{}. key = {}\n".format(index, unichr(key)))
			return key

def solve(cipher, key):
	count = 0
	key_length = len(key)
	message = ''
	for char in cipher:
		message += unichr(key[count % key_length] ^ int(char))
		count += 1
	# print(message)
	return message

with open('59.txt', 'r') as f:
	cipher = f.readlines()[0].split(',')
	key = []
	for index in range(0, 3):
		key.append(analyze(cipher, index, 3))
	message = solve(cipher, key)
	# print(sum([ord(char) for char in message]))