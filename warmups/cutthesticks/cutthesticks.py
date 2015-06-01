from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line.strip())
	sticks_string_list = lines[1].split()
	sticks_list = list()
	for stick_length in sticks_string_list:
		sticks_list.append(int(stick_length))
	print_num_sticks_cut(sticks_list)

def print_num_sticks_cut(sticks):
	sorted_sticks = sorted(sticks)
	min_length = 0
	if len(sorted_sticks) > 0:
		min_length = sorted_sticks[0]
	else:
		return
	reduced_sticks = list()
	num_ops = 0
	for stick in sorted_sticks:
		if min_length > 0:
			if (stick - min_length) > 0:
				reduced_sticks.append(stick - min_length)
			num_ops += 1
	print num_ops
	if len(reduced_sticks) > 0:
		print_num_sticks_cut(reduced_sticks)
	return

if __name__ == '__main__':
	main()