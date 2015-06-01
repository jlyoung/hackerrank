from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line)
	num_of_lines = int(lines[0])
	for line in lines[1:num_of_lines+1]:
		string_operands = line.split(' ')
		int_operands = list()
		for operand in string_operands:
			int_operands.append(int(operand))
		print sum(int_operands)

def sum(operands):
	result = 0
	for operand in operands:
		result += operand
	return result


if __name__ == '__main__':
	main()