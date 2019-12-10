import getopt
import common
from sys      import exit, argv
from os.path  import join
from tqdm     import tqdm

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

	src_dir = '{}\\test_{}\\'.format(src_dir, source)
	with tqdm(total = 7) as pbar:
		pbar.write("Cantata dir: {}".format(src_dir))
		pbar.write("Source name: {}".format(source))
		pbar.write("Worksheet  : {}".format(worksheet))
		# Get working sheet
		ws = common.load_worksheet('{}'.format(join(inputdir, inputfile)), worksheet)
		pbar.update(1)
		# Create test program

		pbar.update(1)
		pbar.update(1)
		pbar.update(1)
		pbar.update(1)

		#Create file dot h, contain all the test case
		common.create_test_case_file(ws, worksheet, src_dir, source, check_sequence)
		pbar.update(1)
		#Create stub function
		# common.create_stub_file(ws, worksheet, src_dir, source)
		pbar.update(1)

if __name__ == "__main__":
	main(argv[1:])