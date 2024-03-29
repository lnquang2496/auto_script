import getopt
import common
from sys      import exit, argv

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

	data1 = '''\
#include <stdio.h>
#include <unistd.h>
#define UTS_NON0 1
#define DONTCARE 0xABCD
'''

	data1_old = '''\
#include <stdio.h>
#include <unistd.h>
#define UTS_NON0 1
#define DONTCARE 0xABCD

#undef IMR_IODEV_IMRCH0
#undef IMR_IODEV_IMRCH1
#undef IMR_IODEV_IMRCH2
#undef IMR_IODEV_IMRCH3
#undef IMR_IODEV_IMRCH4
#undef IMR_IODEV_IMRCH5

#define IMR_IODEV_IMRCH0   (700U)
#define IMR_IODEV_IMRCH1   (701U)
#define IMR_IODEV_IMRCH2   (702U)
#define IMR_IODEV_IMRCH3   (703U)
#define IMR_IODEV_IMRCH4   (704U)
#define IMR_IODEV_IMRCH5   (705U)

#undef IMR_TASK_TMO_CH0
#undef IMR_TASK_TMO_CH1
#undef IMR_TASK_TMO_CH2
#undef IMR_TASK_TMO_CH3
#undef IMR_TASK_TMO_CH4
#undef IMR_TASK_TMO_CH5

#define IMR_TASK_TMO_CH0   (706U)
#define IMR_TASK_TMO_CH1   (707U)
#define IMR_TASK_TMO_CH2   (708U)
#define IMR_TASK_TMO_CH3   (709U)
#define IMR_TASK_TMO_CH4   (710U)
#define IMR_TASK_TMO_CH5   (711U)

#undef IMR_CLK_TMO_CH0
#undef IMR_CLK_TMO_CH1
#undef IMR_CLK_TMO_CH2
#undef IMR_CLK_TMO_CH3
#undef IMR_CLK_TMO_CH4
#undef IMR_CLK_TMO_CH5

#define IMR_CLK_TMO_CH0    (712U)
#define IMR_CLK_TMO_CH1    (713U)
#define IMR_CLK_TMO_CH2    (714U)
#define IMR_CLK_TMO_CH3    (715U)
#define IMR_CLK_TMO_CH4    (716U)
#define IMR_CLK_TMO_CH5    (717U)

#undef IMR_SEM_TMO_CH0
#undef IMR_SEM_TMO_CH1
#undef IMR_SEM_TMO_CH2
#undef IMR_SEM_TMO_CH3
#undef IMR_SEM_TMO_CH4
#undef IMR_SEM_TMO_CH5

#define IMR_SEM_TMO_CH0    (718U)
#define IMR_SEM_TMO_CH1    (719U)
#define IMR_SEM_TMO_CH2    (720U)
#define IMR_SEM_TMO_CH3    (721U)
#define IMR_SEM_TMO_CH4    (722U)
#define IMR_SEM_TMO_CH5    (723U)

#undef IMR_SEM_STATE_CH0
#undef IMR_SEM_STATE_CH1
#undef IMR_SEM_STATE_CH2
#undef IMR_SEM_STATE_CH3
#undef IMR_SEM_STATE_CH4
#undef IMR_SEM_STATE_CH5

#define IMR_SEM_STATE_CH0  (724U)
#define IMR_SEM_STATE_CH1  (725U)
#define IMR_SEM_STATE_CH2  (726U)
#define IMR_SEM_STATE_CH3  (727U)
#define IMR_SEM_STATE_CH4  (728U)
#define IMR_SEM_STATE_CH5  (729U)

#undef IMR_SEM_SYNC_CH0
#undef IMR_SEM_SYNC_CH1
#undef IMR_SEM_SYNC_CH2
#undef IMR_SEM_SYNC_CH3
#undef IMR_SEM_SYNC_CH4
#undef IMR_SEM_SYNC_CH5

#define IMR_SEM_SYNC_CH0   (730U)
#define IMR_SEM_SYNC_CH1   (731U)
#define IMR_SEM_SYNC_CH2   (732U)
#define IMR_SEM_SYNC_CH3   (733U)
#define IMR_SEM_SYNC_CH4   (734U)
#define IMR_SEM_SYNC_CH5   (735U)
'''

	data2 = '''\
	int ret;
	char *buffer;

	buffer = (char*)malloc(16*1024*1024);
	memset(buffer, 0, 16*1024*1024);
	fflush(stdout);
	dup(STDOUT_FILENO);
	freopen("NUL", "a", stdout);

	setvbuf(stdout, buffer, _IOFBF, 16*1024*1024);


'''
	data3 = '''\

	run_tests();

	ret = !END_SCRIPT(true);
	return ret;
'''

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

	start_pos = ["/* Program Entry Point                                                       */",\
					"/*****************************************************************************/"]
	common.file_append(src_dir, "test_{}.c".format(source), data1, start_pos)

	start_pos = ["int main()", "{"]
	common.file_append(src_dir, "test_{}.c".format(source), data2, start_pos)

	start_pos = ["OPEN_LOG", "START_SCRIPT"]
	common.file_append(src_dir, "test_{}.c".format(source), data3, start_pos)

	# Clear test program
	start_pos = ["/* Prototypes for test functions */",\
				 "void run_tests();"]
	end_pos = ["/*****************************************************************************/"]
	common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

	start_pos = ["/* Test Control                                                              */",\
				 "void run_tests()",\
				 "{"]
	end_pos = ["rule_set(\"*\", \"*\");"]
	common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)

	start_pos = ["/* Test Cases                                                                */",\
				 "/*****************************************************************************/", "\n"]
	end_pos = ["\n", "/*****************************************************************************/"]
	common.file_clear(src_dir, "test_{}.c".format(source), start_pos, end_pos)


if __name__ == "__main__":
	main(argv[1:])