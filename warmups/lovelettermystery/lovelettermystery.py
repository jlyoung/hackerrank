from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line)
	num_of_lines = int(lines[0])
	for line in lines[1:num_of_lines+1]:
		print get_num_of_ops(line.strip())

def get_num_of_ops(line):
	total_num_of_ops = 0
	line_list = list(line)
	line_length = len(line_list)
	for i in range(0, (line_length/2)):
		corresponding_ending = i+1
		if line_list[i] != line_list[-corresponding_ending]:
			total_num_of_ops += abs(ord(line_list[-corresponding_ending]) - ord(line_list[i]))
	return total_num_of_ops


if __name__ == '__main__':
	main()