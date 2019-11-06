void test_r_imr_osal_sem_lock(){
	struct CPPTH_LOOP_INPUT_STRUCT {
		/* Test case data declarations */
		char* name;
		char* description;
		char* expected_calls;
		int32_t index;
		int32_t * index3;
		struct abc * struct_t;
		int a;
		int * b;

		int32_t expected_returnValue;
	};
	int32_t returnValue;
	/* Import external data declarations */
	#include "test_r_imr_osal_sem_lock.h"

	/* Set global data */
	initialise_global_data();
	/* Set expected values for global data checks */
	initialise_expected_global_data();


	int32_t  local_index3;
	struct abc  local_struct_t;

	START_TEST_LOOP();
		/* Expected Call Sequence  */
		EXPECTED_CALLS(CURRENT_TEST.expected_calls);

			if (CURRENT_TEST.index3 != NULL) {
				CURRENT_TEST.index3 = &local_index3;
			}
			if (CURRENT_TEST.struct_t != NULL) {
				CURRENT_TEST.struct_t = &local_struct_t;
			}
			CURRENT_TEST.struct_t->a = CURRENT_TEST.a;
			CURRENT_TEST.struct_t->b = CURRENT_TEST.b;
			/* Call SUT */
			returnValue = r_imr_osal_sem_lock();

			/* Test case checks */
			CHECK_S_INT(returnValue, CURRENT_TEST.expected_returnValue);

			CHECK_S_INT(local_index3, CURRENT_TEST.index3);
			CHECK_S_INT(local_abcstruct_t, CURRENT_TEST.abcstruct_t);
		END_CALLS();
	END_TEST_LOOP();
}

