import getopt
import common
from sys import exit

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

        data1 = ["#include <stdio.h>\n#include <unistd.h>\n#define UTS_NON0 1\n"]
        data2 = ['''\
	int ret;
	char *buffer;

	buffer = (char*)malloc(16*1024*1024);
	memset(buffer, 0, 16*1024*1024);
	fflush(stdout);
	dup(STDOUT_FILENO);
	freopen("NUL", "a", stdout);

	setvbuf(stdout, buffer, _IOFBF, 16*1024*1024);


''']
        data3 = ['''\

	run_tests();

	ret = !END_SCRIPT(true);
	return ret;
''']

        start_pos = ["/* Program Entry Point                                                       */",\
                     "/*****************************************************************************/"]
        end_pos = ["int main()"]
        common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

        start_pos = ["int main()", "{"]
        end_pos = ["OPEN_LOG"]
        common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

        start_pos = ["OPEN_LOG", "START_SCRIPT"]
        end_pos = ["}"]
        common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

        common.file_append(src_dir, "test_{}.c".format(source), data1, start_pos)

        start_pos = ["int main()", "{"]
        common.file_append(src_dir, "test_{}.c".format(source), data2, start_pos)

        start_pos = ["OPEN_LOG", "START_SCRIPT"]
        common.file_append(src_dir, "test_{}.c".format(source), data2, start_pos)

if __name__ == "__main__":
	main(sys.argv[1:])