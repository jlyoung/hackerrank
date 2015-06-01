from sys import stdin

def main():
	operands = list()
	for line in stdin:
		operands.append(int(line.strip()))
	print sum(operands)

def sum(operands):
	result = 0
	for op in operands:
		result += op
	return result

if __name__ == '__main__':
	main()