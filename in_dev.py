from openpyxl import load_workbook
from os       import rename, remove
from sys      import exit
from os.path  import isfile, join
from common   import coor_find_cell, get_cell_value, coor_shift_down, coor_shift_right, load_worksheet, row_of_testcase

# Create stub instance
def create_stub_file_new(ws, worksheet:str, src_dir:str, src:str):
	start_row, end_row, testcase_col = row_of_testcase(ws, '#')
	cell_1_left                      = coor_find_cell(ws, 'Input factor')
	cell_1_right                     = coor_find_cell(ws, 'Output element')

	def get_func_name(mark:str, target:str)->str:
		func_full = target.replace(mark, '')
		func_type = func_full[ : func_full.find(' ')]
		func_name = func_full[ func_full.find(' ') + 1 : func_full.find('(')]
		return func_type, func_name

	def get_check_type(val:str)->str:
		type_1 = ['true', 'false', 'UTS_']

		for i in type_1:
			if i in val:
				return 'CHECK_BOOLEAN'

		if '0x' in val:
			if val.endswith('u') or val.endswith('U'):
				return 'CHECK_U_INT'
			else:
				return 'CHECK_S_INT'

		if val.endswith('u') or val.endswith('U'):
			if val.replace('u', '').replace('U', '').isdigit:
				return 'CHECK_U_INT'

		if val.isdigit:
			return 'CHECK_S_INT'

		return 'CHECK_ADDRESS'

	for cur_row in range(start_row, end_row + 1):
		list_of_func = list()
		tc_num = get_cell_value(ws, [testcase_col, cur_row]).replace('-', '_')

		# Input factor process
		cell_2_left = coor_shift_down(ws, cell_1_left)
		while (cell_2_left['lastcol'] <= cell_1_left['lastcol']):
			data_1 = ''
			cell_2_left_val = get_cell_value(ws, cell_2_left)
			######
			if '[rt]' in cell_2_left_val:
				func_type, func_name = get_func_name('[rt]', cell_2_left_val)
				cur_val = get_cell_value(ws, [cell_2_left['firstcol'], cur_row])
				
				# Get return value of funtion
				if cur_val == 'None' or cur_val == '-':
					cur_val = 0
				if 'void' in func_type:
					temp_data = '\treturn;\n'
				else:
					temp_data = '\treturn {};\n'.format(cur_val)
				
				# Check is [f] in the right of [rt]
				temp_cell_2_left = coor_shift_right(ws, cell_2_left)
				temp_cell_2_val  = get_cell_value(ws, temp_cell_2_left)
				if '[f]' in temp_cell_2_val and func_name in temp_cell_2_val:
					cell_2_left = temp_cell_2_left
					cell_3_left = coor_shift_down(ws, cell_2_left)
					while cell_3_left['lastcol'] <= cell_2_left['lastcol']:
						cell_3_left_val = get_cell_value(ws, cell_3_left)
						cur_val = get_cell_value(ws, [cell_3_left['firstcol'], cur_row])

						# Get output value of function
						if cur_val != 'None' and cur_val != '-':
							if 'UTS' in cur_val:
								if cur_val.find(')') != -1:
									cast_type = cur_val[:cur_val.find(')') + 1]
								else:
									cast_type = ''
								if '*' in cell_3_left_val:
									data_1 = '{}\t\t{} = {}&local;\n'.format(data_1, cell_3_left_val, cast_type)
								else:
									data_1 = '{}\t\t*{} = {}&local;\n'.format(data_1, cell_3_left_val, cast_type)
							else:
								if '*' in cell_3_left_val:
									data_1 = '{}\t\t{} = {};\n'.format(data_1, cell_3_left_val, cur_val)
								else:
									data_1 = '{}\t\t*{} = {};\n'.format(data_1, cell_3_left_val, cur_val)

						cell_3_left = coor_shift_right(ws, cell_3_left)

			cell_2_left = coor_shift_right(ws, cell_2_left)
		# Output element process
		cell_2_right = coor_shift_down(ws, cell_1_right)
		while (cell_2_right['lastcol'] <= cell_1_right['lastcol']):
			cell_2_right_val = get_cell_value(ws, cell_2_right)
			######
			if '[f]' in cell_2_right_val:
				func_type, func_name = get_func_name('[f]', cell_2_right_val)
				cell_3_right = coor_shift_down(ws, cell_2_right)
				while cell_3_right['lastcol'] <= cell_2_right['lastcol']:
					cur_val = get_cell_value(ws, [cell_3_right['firstcol'], cur_row])
					print(cur_val)
					if cur_val != 'None' and cur_val != '-':
						check_type = get_check_type(cur_val):
						
					cell_3_right = coor_shift_right(ws, cell_3_right)
			cell_2_right = coor_shift_right(ws, cell_2_right)

		final_data = """\
{data_1}
{data_2}
"""

ws = load_worksheet('in_dev.xlsx', 'Sheet1')
create_stub_file_new(ws, 'Sheet1', '', '')