from sys import stdin

def main():
	operands = list()
	for line in stdin:
		operands.append(int(line.strip()))
	print get_max_xor_value(operands[0], operands[1])

def get_max_xor_value(a, b):
	max_val = 0
	for opa in range(a, b+1):
		for opb in range(a, b+1):
			xor_val = (opa ^ opb)
			if  xor_val > max_val:
				max_val = xor_val
	return max_val

if __name__ == '__main__':
	main()