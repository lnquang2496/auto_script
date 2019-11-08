from common import coor_find_cell, get_cell_value, coor_shift_right, coor_shift_left, coor_shift_up, coor_shift_down, load_worksheet,\
	get_type_name, check_pointer, check_structure, select_check_type

def pcl_to_testprogram(ws):
	list_of_input = []
	data_1 = ''
	data_2 = ''
	data_3 = ''
	data_4 = ''

	cell_1 = coor_find_cell(ws, 'Input factor')
	cell_2 = coor_shift_down(ws, cell_1)
	while cell_2['lastcol'] <= cell_1['lastcol']:
		cell_2_val = get_cell_value(ws, cell_2)

		if '[g]' in cell_2_val:
			is_global = True
		else:
			is_global = False

		if '[a]' in cell_2_val:
			is_argument = True
		else:
			is_argument = False

		if is_global == True or is_argument == True:
			cell_2_val = cell_2_val.replace('[a]', '').replace('[g]', '')
			cell_2_type, cell_2_name = get_type_name(ws, cell_2_val)
			is_cell_2_pointer = check_pointer(ws, cell_2_val)
			is_cell_2_structure = check_structure(ws, cell_2_val)
			exist = False

			if cell_2_name not in list_of_input:
				list_of_input.append(cell_2_name)
			else:
				exist = True
			###
			if exist == False and is_global == False:
				temp_data = '\t\t{};\n'.format(cell_2_val.replace('[a]', '').replace('[g]', '').replace(';', ''))
				data_1 = '{}{}'.format(data_1, temp_data)

			if (cell_2['lastcol'] - cell_2['firstcol'] == 0) and (exist == False):
				'''NOT MERGED CELL'''

				if is_cell_2_pointer:
					###
					temp_data = '\t{} local_{};\n'.format(cell_2_type, cell_2_name)
					data_2 = '{}{}'.format(data_2, temp_data)
					###
					temp_data = '\t\tif (CURRENT_TEST.{name} != NULL){{\n\t\t\t CURRENT_TEST.{name} = &local_{name};\n\t\t}}\n'.format(name = cell_2_name)
					data_3 = '{}{}'.format(data_3, temp_data)
				pass

			else:
				'''IS MERGED CELL'''
				cell_2_number = ''
				if '[' in cell_2_val:
					cell_2_number = '_{}'.format(cell_2_val[cell_2_val.find('[') + 1 : cell_2_val.find(']')])
					cell_2_val = cell_2_val.replace('[', '_').replace(']', '')

				cell_3 = coor_shift_down(ws, cell_2)
				while cell_3['lastcol'] <= cell_2['lastcol']:
					cell_3_val = get_cell_value(ws, cell_3)
					cell_3_type, cell_3_name = get_type_name(ws, cell_3_val)
					is_cell_3_pointer = check_pointer(ws, cell_3_val)
					is_cell_3_structure = check_structure(ws, cell_3_val)
					###
					if '[' in cell_3_name:
						cell_2_number = '{}{}'.format(cell_2_number, cell_3_name[cell_3_name.find('['):])
						cell_3_name = cell_3_name[: cell_3_name.find('[')]
					###
					if '[' in cell_3_val:
						cell_3_val = cell_3_val[: cell_3_val.find('[')]
					temp_data = '\t\t{}{};\n'.format(cell_3_val, cell_2_number)
					data_1 = '{}{}'.format(data_1, temp_data)

					if is_cell_3_pointer:
						###
						temp_data = '\t{} local_{};\n'.format(cell_3_type, cell_3_name)
						data_2 = '{}{}'.format(data_2, temp_data)
						###
						temp_data = '\t\tif (CURRENT_TEST.{name}{number} != NULL){{\n\t\t\t CURRENT_TEST.{name}{number} = &local_{name};\n\t\t}}\n'.format(name = cell_3_name, number = cell_2_number)
						data_3 = '{}{}'.format(data_3, temp_data)
					###
					if is_global:
						if is_cell_3_pointer:
							access = '->'
						else:
							access = '.'
						temp_data = '\t\t{}{}{} = CURRENT_TEST.{}{};\n'.format(cell_2_name, access, cell_3_name.replace(';', ''), cell_3_name.replace(';', ''), cell_2_number)
						data_3 = '{}{}'.format(data_3, temp_data)


					cell_3 = coor_shift_right(ws, cell_3)
				pass
		cell_2 = coor_shift_right(ws, cell_2)

	del list_of_input

	cell_1 = coor_find_cell(ws, 'Output element')
	cell_2 = coor_shift_down(ws, cell_1)
	while cell_2['lastcol'] <= cell_1['lastcol']:
		cell_2_val = get_cell_value(ws, cell_2)

		if '[g]' in cell_2_val:
			is_global = True
			cell_2_val = cell_2_val.replace('[g]', '')
		else:
			is_global = False

		if '[a]' in cell_2_val:
			is_argument = True
			cell_2_val = cell_2_val.replace('[a]', '')
		else:
			is_argument = False

		if is_global == True or is_argument == True:
			cell_2_type, cell_2_name = get_type_name(ws, cell_2_val)
			is_cell_2_pointer = check_pointer(ws, cell_2_val)
			is_cell_2_structure = check_structure(ws, cell_2_val)

			if cell_2['lastcol'] - cell_2['firstcol'] == 0:

				if is_cell_2_pointer:
					###
					temp_data = '\t\t{} expected_{};\n'.format(cell_2_type, cell_2_name)
					data_1 = '{}{}'.format(data_1, temp_data)

					init_val = get_cell_value(ws, coor_shift_down(ws, cell_2))
					if init_val != '-' and init_val != None:
						###
						temp_data = '\tlocal_{} = {};\n'.format(cell_2_name, init_val)
						data_2 = '{}{}'.format(data_2, temp_data)

					###
					check_type = select_check_type(ws, cell_2_val)
					temp_data = '\t\t\t{check}({left}, {right});\n'.format(\
						check = check_type,\
						left = 'local_{}'.format(cell_2_name),\
						right = 'CURRENT_TEST.expected_{}'.format(cell_2_name)\
					)
					data_4 = '{}{}'.format(data_4, temp_data)

				pass
			else:
				'''IS MERGED CELL'''
				cell_2_number = ''
				if '[' in cell_2_val:
					cell_2_number = '_{}'.format(cell_2_val[cell_2_val.find('[') + 1 : cell_2_val.find(']')])
					cell_2_val = cell_2_val.replace('[', '_').replace(']', '')

				cell_3 = coor_shift_down(ws, cell_2)
				while cell_3['lastcol'] <= cell_2['lastcol']:
					cell_3_val = get_cell_value(ws, cell_3)
					cell_3_type, cell_3_name = get_type_name(ws, cell_3_val)
					is_cell_3_pointer = check_pointer(ws, cell_3_val)
					is_cell_3_structure = check_structure(ws, cell_3_val)

					###
					if '[' in cell_3_name:
						cell_2_number = '{}{}'.format(cell_2_number, cell_3_name[cell_3_name.find('['):])
						cell_3_name = cell_3_name[: cell_3_name.find('[')]

					temp_data = '\t\t{} expected_{}{};\n'.format(cell_3_type, cell_3_name, cell_2_number)
					data_1 = '{}{}'.format(data_1, temp_data)

					###
					if is_global:

						if is_cell_3_pointer:
							access = '->'
						else:
							access = '.'
						check_type = select_check_type(ws, cell_3_val)
						temp_data = '\t\t\t{check}({left}, {right});\n'.format(\
							check = check_type,\
							left = '{}{}{}'.format(cell_2_name, access, cell_3_name),\
							right = 'CURRENT_TEST.expected_{}{}'.format(cell_3_name, cell_2_number)\
						)
						data_4 = '{}{}'.format(data_4, temp_data)

					cell_3 = coor_shift_right(ws, cell_3)
				pass

		cell_2 = coor_shift_right(ws, cell_2)

	return data_1[:-1], data_2, data_3, data_4
'''
sheet_name = "file_name_3"
ws = load_worksheet("sample.xlsx", sheet_name)
for p in pcl_to_testprogram(ws):
	print(p)
print("----DONE----")
'''
def get_input_argument(ws, top_cell_name:str, target:str)->str:
	valid_top_cell_name = ['Input factor', 'Output element']
	valid_target = ['[a]', '[f]', '[rt]', '[g]']
	if (target not in valid_target) or (top_cell_name not in valid_top_cell_name):
		return
	del valid_top_cell_name, valid_target

	cell_1 = coor_find_cell(ws, top_cell_name)
	cell_2 = coor_shift_down(ws, cell_1)
	data = ''
	list_of_handle = []
	while (cell_2['lastcol'] <= cell_1['lastcol']):
		### Begin of while
		cell_2_val = get_cell_value(ws, cell_2)
		if target in cell_2_val:
			cell_2_type, cell_2_name = get_type_name(ws, cell_2_val)
			is_cell_2_pointer = check_pointer(ws, cell_2_val)
			is_cell_2_structure = check_structure(ws, cell_2_val)
			if cell_2_name in list_of_handle:
				pass
			else:
				list_of_handle.append(cell_2_name)
				data_append = 'CURRENT_TEST.{},'.format(cell_2_name)
				data = '{}{}'.format(data, data_append)

		###	Next of while
		cell_2 = coor_shift_right(ws, cell_2)
	return data[:-1]
	pass

def test_part(ws, func_name:str)->str:
	data_1, data_2, data_3, data_4 = pcl_to_testprogram(ws)
	input_argument = get_input_argument(ws, 'Input factor', '[a]')
	data = '''\
void test_{func_name}(){{
	struct CPPTH_LOOP_INPUT_STRUCT {{
		/* Test case data declarations */
		char* name;
		char* description;
		char* expected_calls;
		int execute;
{data_1}
		int32_t expected_returnValue;
	}};
	int32_t returnValue;
	/* Import external data declarations */
	#include "test_{func_name}.h"

	/* Set global data */
	initialise_global_data();
	/* Set expected values for global data checks */
	initialise_expected_global_data();

{data_2}

	START_TEST_LOOP();
		/* Expected Call Sequence  */
		EXPECTED_CALLS(CURRENT_TEST.expected_calls);
{data_3}
			/* Call SUT */
			returnValue = {func_name}({input_argument});

			/* Test case checks */
			CHECK_S_INT(returnValue, CURRENT_TEST.expected_returnValue);
{data_4}
		END_CALLS();
	END_TEST_LOOP();
}}
'''.format(\
	func_name = func_name,\
	data_1 = data_1,\
	data_2 = data_2,\
	data_3 = data_3,\
	data_4 = data_4,\
	input_argument = input_argument\
	)
	print(data)
	return data
