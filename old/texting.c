void test_r_imr_osal_init(){
	struct CPPTH_LOOP_INPUT_STRUCT {
		/* Test case data declarations */
		char* name;
		char* description;
		char* expected_calls;
		uint32_t a;
		int32_t b;;
		int32_t * c;
		uint32_t * d;
		struct_abc abc_name;
		uint32_t f;
		uint32_t g;		int32_t expected_c;
		uint32_t expected_d;
		int32_t expected_returnValue;
	};
	int32_t returnValue;
	/* Import external data declarations */
	#include "test_r_imr_osal_init.h"

	/* Set global data */
	initialise_global_data();
	/* Set expected values for global data checks */
	initialise_expected_global_data();

	int32_t local_c;
	uint32_t local_d;

	START_TEST_LOOP();
		/* Expected Call Sequence  */
		EXPECTED_CALLS(CURRENT_TEST.expected_calls);
			if (CURRENT_TEST.c != NULL) {
				CURRENT_TEST.c = &local_c;
			}
			if (CURRENT_TEST.d != NULL) {
				CURRENT_TEST.d = &local_d;
			}
			CURRENT_TEST.abc_name.f = CURRENT_TEST.f;
			CURRENT_TEST.abc_name.g = CURRENT_TEST.g;

			/* Call SUT */
			returnValue = r_imr_osal_init(CURRENT_TEST.a,CURRENT_TEST.b,CURRENT_TEST.c,CURRENT_TEST.d,CURRENT_TEST.abc_name);

			/* Test case checks */
			CHECK_S_INT(returnValue, CURRENT_TEST.expected_returnValue);
			CHECK_S_INT(local_c, CURRENT_TEST.expected_c);
			CHECK_U_INT(local_d, CURRENT_TEST.expected_d);

		END_CALLS();
	END_TEST_LOOP();
}
