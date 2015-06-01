from collections import Counter
from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line.strip())
	size_of_array = int(lines[0])
	line_two_array = lines[1].split()
	print find_lonely_int(line_two_array)

def find_lonely_int(int_array):
	lonely_int = None
	counter = Counter(int_array)
	for k,v in counter.iteritems():
		if v == 1:
			lonely_int = k
			break
	return lonely_int

if __name__ == '__main__':
	main()