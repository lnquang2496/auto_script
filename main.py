import getopt
import common
from sys      import exit
from os.path  import join

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hid:i:ws:sr:se:ca:",["idir=","ifile=","wsheet=","source=","check_seq=","can_dir="])
	except getopt.GetoptError:
		print("--idir <inputfir> --ifile <inputfile> --wsheet <worksheet> --check_seq <True/False> --source <source>")
		exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("--idir <inputfir> --ifile <inputfile> --wsheet <worksheet> --check_seq <True/False> --source <source>")
			exit()
		elif opt in ("-id", "--idir"):
			inputdir = arg
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-ws", "--wsheet"):
			worksheet = arg
		elif opt in ("-sr", "--source"):
			source = arg
		elif opt in ("-se", "--check_seq"):
			if ('rue' in arg):
				check_sequence = True
			else:
				check_sequence = False
		elif opt in ("-ca", "--can_dir"):
			src_dir = arg 

		src_dir = '{}test_{}\\'.format(src_dir, source)
		# Get working sheet
		ws = common.load_worksheet('{}'.format(join(inputdir, inputfile)), worksheet)
        # Create test program
        data = common.create_test_program(ws, worksheet)
        start_pos = ["void test_{}(){{".format(worksheet)]
        end_pos = ["END_TEST_LOOP();", "}"]
        common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

        common.file_append(src_dir, "test_{}.c".format(source), data, start_pos)
		# Create file dot h, contain all the test case
		common.create_test_case_file(ws, worksheet, src_dir, source, check_sequence)
		# Create stub function
		common.create_stub_file(ws, worksheet, src_dir, source)

if __name__ == "__main__":
	main(sys.argv[1:])