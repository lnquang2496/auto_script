import os, sys, getopt

# Main function
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hca:src:",["can_dir=","source=",])
	except getopt.GetoptError:
		print("--")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("--")
			sys.exit()
		elif opt in ("-ca", "--can_dir"):
			can_dir = arg + '\\'
		elif opt in ("-src", "--source"):
			src = arg

	can_dir = can_dir + 'test_' + src + '\\'
	position = ['IF_INSTANCE(\"default\")', '}', 'LOG_SCRIPT_ERROR']
	count = 0
	os.rename(can_dir + 'test_' + src + '.c', can_dir + 'temp.txt')
	infile = open(can_dir + 'temp.txt', 'r')
	outfile = open(can_dir + 'test_' + src + '.c', 'w')
	for line in infile:

		if (count == 2):
			if (position[2] in line):
				outfile.write(line)
				count = 0
		else:
			outfile.write(line)

		if count < 2:
			if (position[count] in line):
				count += 1

	infile.close()
	outfile.close()
	os.remove(can_dir + 'temp.txt')


if __name__ == "__main__":
	main(sys.argv[1:])
