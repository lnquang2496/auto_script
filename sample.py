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
