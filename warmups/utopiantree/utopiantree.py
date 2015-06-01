from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line)
	num_of_lines = int(lines[0])
	for line in lines[1:num_of_lines+1]:
		print compute_height(int(line.strip()))

def compute_height(cycles):
	result = 1
	for i in range(1,cycles+1):
		if i % 2 == 1:
			result = result * 2
		else:
			result += 1
	return result


if __name__ == '__main__':
	main()