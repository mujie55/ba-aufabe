def read_file(filename):
	lines = []
	with open(filename, 'r')as f:
		for line in f:
			lines.append(line.strip(). split())
	return lines
	lins = read_file()

#def coverd(lines):
	new = []
	for line in lines:
		print(line)
	return new

def write_file(filename, lines):
	with open (filename, 'w')as f:
		for line in lines:
			f.write(str(line) + '\n')

def main():
	lines = read_file('123.txt')
	print(lines)
	#lines = coverd(lines)
	write_file('123.csv', lines)
main()



