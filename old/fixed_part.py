import os, sys, getopt

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
	can_dir = '{}test_{}\\'.format(can_dir, src)
	file_dir = '{}test_{}.c'.format(can_dir, src)

	src_name = 'test_{}.c'.format(src)
	data = \
'''/******************************************************************************/
/*                            Cantata Test Script                            */
/*****************************************************************************/
/*
*    Filename: test_r_imr_osal_ctl.c
*    Author: quangla
*    Generated on: 05-Nov-2019 18:24:04
*    Generated from: r_imr_osal_ctl.c
*/
/*****************************************************************************/
/* Environment Definition                                                    */
/*****************************************************************************/

#define TEST_SCRIPT_GENERATOR 2

/* Include files from software under test */
#include <stdio.h>
#include <unistd.h>
#include <INTEGRITY.h>
#include "TBD.h"
#define CANTATA_DEFAULT_VALUE 0
/* Default value of variables & stub returns */

#include <cantpp.h>  /* Cantata Directives */
/* pragma qas cantata testscript start */
/*****************************************************************************/
/* Global Data Definitions                                                   */
/*****************************************************************************/
#define UTS_NON0 1U
#undef IMR_IODEV_IMRCH0
#undef IMR_IODEV_IMRCH1
#undef IMR_IODEV_IMRCH2
#undef IMR_IODEV_IMRCH3
#undef IMR_IODEV_IMRCH4
#undef IMR_IODEV_IMRCH5
#define IMR_IODEV_IMRCH0 700U
#define IMR_IODEV_IMRCH1 701U
#define IMR_IODEV_IMRCH2 702U
#define IMR_IODEV_IMRCH3 703U
#define IMR_IODEV_IMRCH4 704U
#define IMR_IODEV_IMRCH5 705U
/* Global Functions *

/* Global data */
/* None */

/* Expected variables for global data */
/* None */

/* This function initialises global data to default values. This function       */
/* is called by every test case so must not contain test case specific settings */
static void initialise_global_data(){
	TEST_SCRIPT_WARNING("Verify initialise_global_data()\n");
	/* No global data */
}

/* This function copies the global data settings into expected variables for */
/* use in check_global_data(). It is called by every test case so must not   */
/* contain test case specific settings.                                      */
static void initialise_expected_global_data(){
	TEST_SCRIPT_WARNING("Verify initialise_expected_global_data()\n");
	/* No global data */
}

/* This function checks global data against the expected values. */
static void check_global_data(){
	TEST_SCRIPT_WARNING("Verify check_global_data()\n");
	/* No global data */
}

/* Prototypes for test functions */
void run_tests();/

/*****************************************************************************/
/* Coverage Analysis                                                         */
/*****************************************************************************/
/* Coverage Rule Set: 100% Entry Point + Statement + Call Return + Decision Coverage */
static void rule_set(char* cppca_sut,
					char* cppca_context)
{
	START_TEST("COVERAGE RULE SET",
			"100% Entry Point + Statement + Call Return + Decision Coverage");
#ifdef CANTPP_SUBSET_DEFERRED_ANALYSIS
	TEST_SCRIPT_WARNING("Coverage Rule Set ignored in deferred analysis mode\n");
#elif CANTPP_COVERAGE_INSTRUMENTATION_DISABLED
	TEST_SCRIPT_WARNING("Coverage Instrumentation has been disabled\n");
#elif CANTPP_INSTRUMENTATION_DISABLED
	TEST_SCRIPT_WARNING("Instrumentation has been disabled\n");
#else
	ANALYSIS_CHECK("100% Entry Point Coverage",
				cppca_entrypoint_cov,
				100.0);
	
	ANALYSIS_CHECK("100% Statement Coverage",
				cppca_statement_cov,
				100.0);
	
	ANALYSIS_CHECK("100% Call Return Coverage",
				cppca_callreturn_cov,
				100.0);
	
	ANALYSIS_CHECK("100% Decision Coverage",
				cppca_decision_cov,
				100.0);
	
	REPORT_COVERAGE(cppca_entrypoint_cov|
					cppca_statement_cov|
					cppca_callreturn_cov|
					cppca_decision_cov,
					cppca_sut,
					cppca_all_details|cppca_include_catch,
					cppca_context);
#endif
	END_TEST();
}

/*****************************************************************************/
/* Program Entry Point                                                       */
/*****************************************************************************/
int main()
{
	int ret;
	char *buffer;

	buffer = (char*)malloc(16*1024*1024);
	memset(buffer, 0, 16*1024*1024);
	fflush(stdout);
	dup(STDOUT_FILENO);
	freopen("NUL", "a", stdout);

	setvbuf(stdout, buffer, _IOFBF, 16*1024*1024);


	OPEN_LOG("test_TBD.ctr", false, 100);
	START_SCRIPT("TBD", true);

	run_tests();

	ret = !END_SCRIPT(true);
	return ret;
}

/*****************************************************************************/
/* Test Control                                                              */
/*****************************************************************************/
/* run_tests() contains calls to the individual test cases, you can turn test*/
/* cases off by adding comments*/
void run_tests()
{
	/* TBD_run_tests */
    rule_set("*", "*");
    EXPORT_COVERAGE("test_r_imr_osal_ctl.cov", cppca_export_replace);
}
'''
	with open(src_name, 'w') as f:
		f.writelines(data)

if __name__ == "__main__":
	main(sys.argv[1:])