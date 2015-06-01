from sys import stdin

def main():
	lines = list()
	for line in stdin:
		lines.append(line.strip())
	first_line = lines[0].split()
	freeway_length = int(first_line[0])
	test_cases = int(first_line[1])
	second_line = lines[1].split()
	widths = list()
	for segment in second_line:
		widths.append(int(segment))
	for line in lines[2:test_cases+2]:
		indexes = line.split()
		print get_max_veh_size(int(indexes[0]),int(indexes[1]),widths)

def get_max_veh_size(i, j, widths):
	min_lane_size = 3
	for segment in range(i, j+1):
		if widths[segment] < min_lane_size:
			min_lane_size = widths[segment]
	return min_lane_size

if __name__ == '__main__':
	main()