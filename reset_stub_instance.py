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
			can_dir = '{}\\'.format(arg)
		elif opt in ("-src", "--source"):
			src = arg

	#can_dir = can_dir + 'test_' + src + '\\'
	can_dir = '{}test_{}\\'.format(can_dir, src)
	position = ['IF_INSTANCE(\"default\")', '}', 'LOG_SCRIPT_ERROR']
	count = 0
	#os.rename(can_dir + 'test_' + src + '.c', can_dir + 'temp.txt')
	os.rename('{}test_{}.c'.format(can_dir, src), '{}temp.txt'.format(can_dir))
	#infile = open(can_dir + 'temp.txt', 'r')
	#outfile = open(can_dir + 'test_' + src + '.c', 'w')
	with open('{}temp.txt'.format(can_dir), 'r') as infile, open('{}test_{}.c'.format(can_dir, src), 'w') as outfile:
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

	os.remove(can_dir + 'temp.txt')

if __name__ == "__main__":
	main(sys.argv[1:])
