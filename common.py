import os, sys, getopt
from openpyxl import load_workbook

def coor_find_cell(ws, target, match_case:bool=False, find_all:bool=False):
	return_value = list()
	target_found = False
	# If target is string type
	if isinstance(target, str):
		for rows in ws:
			for cell in rows:
				if match_case:
					target_found = target in cell.value
				else:
					target_found = target == cell.value

				if target_found:
					not_merged_cell = True
					for merged_cell in ws.merged_cells:
						if (cell.coordinate in merged_cell):
							temp = {'firstcol':merged_cell.bounds[0],
									'firstrow':merged_cell.bounds[1],
									'lastcol':merged_cell.bounds[2],
									'lastrow':merged_cell.bounds[3]}
							not_merged_cell = False
							if find_all:
								return_value.append(temp)
							else:
								return dict(temp)
					if not_merged_cell:
						temp = {'firstcol':cell.column,
								'firstrow':cell.row,
								'lastcol':cell.column,
								'lastrow':cell.row}
						if find_all:
							return_value.append(temp)
						else:
							return dict(temp)
	# If target is list type, list format [column, row]
	elif isinstance(target, list):
		# list  = [col, row]
		coor = ws.cell(column=target[0], row=target[1]).coordinate
		not_merged_cell = True
		for merged_cell in ws.merged_cells:
			if (coor in merged_cell):
				temp = {'firstcol':merged_cell.bounds[0],
						'firstrow':merged_cell.bounds[1],
						'lastcol':merged_cell.bounds[2],
						'lastrow':merged_cell.bounds[3]}
				not_merged_cell = False
				return dict(temp)
		if not_merged_cell:
			temp = {'firstcol':target[0],
					'firstrow':target[1],
					'lastcol':target[0],
					'lastrow':target[1]}
			return dict(temp)
	return return_value

def get_cell_value(ws, coor)->str:
	if isinstance(coor, list):
		val = ws.cell(column=coor[0], row=coor[1]).value
		return str(val)
	else:
		for row in range (coor['firstrow'], coor['lastrow'] + 1):
			for col in range (coor['firstcol'], coor['lastcol'] + 1):
				val = ws.cell(column=col, row=row).value
				if (val != None):
					return str(val)
	return None

def coor_shift_right(ws, coor):
	temp = list([coor['lastcol'] + 1, coor['firstrow']])
	return coor_find_cell(ws, temp)

def coor_shift_left(ws, coor):
	col = coor['firstcol'] - 1
	if col < 1:
		col = 1
	temp = list([col, coor['firstrow']])
	return coor_find_cell(ws, temp)

def coor_shift_up(ws, coor):
	row = coor['firstrow'] - 1
	if row < 1:
		row = 1
	temp = list([coor['firstcol'], row])
	return coor_find_cell(ws, temp)

def coor_shift_down(ws, coor):
	temp = list([coor['firstcol'], coor['lastrow'] + 1])
	return coor_find_cell(ws, temp)

def load_worksheet(filename:str, sheetname:str):
	try:
		wb = load_workbook(filename, data_only=True)
	except:
		sys.exit(0)
	ws = wb[sheetname]
	return ws

def count_cell_in_merged_cell(ws, cell_1)->int:
	count = 0
	cell_2 = coor_shift_down(ws, cell_1)
	while cell_2['lastcol'] <= cell_1['lastcol']:
		count += 1
		cell_2 = coor_shift_right(ws, cell_2)
	return count

def get_type_name(ws, value:str)->str:
	temp_val = value.replace('[a]', '').replace('[g]', '').\
		replace('*', '').replace(';', '').replace('  ', ' ')
	all_val = temp_val.split(' ')
	cell_name = all_val[len(all_val) - 1]
	cell_type = ''
	for i in range(len(all_val) - 1):
		cell_type = '{}{} '.format(cell_type, all_val[i])
	return cell_type[:-1], cell_name

def check_pointer(ws, value:str)->bool:
	valid_pointer = ['*', 'IODevice ', 'DevTree_Node']
	for x in valid_pointer:
		if x in value:
			return True
	return False

def check_structure(ws, value:str)->bool:
	valid_structure= ['struct', 'imr_state_mng', 'imr_rtt_state_mng', 'imr_struct_t']
	for x in valid_structure:
		if x in value:
			return True
	return False

def select_check_type(ws, value:str)->str:
	check_address = ['IODevice ']
	check_u_int = ['uint', 'unsigned', 'Address']
	check_bool = ['bool', 'Boolean']
	# default check type is CHECK_S_INT
	check_type = 'CHECK_S_INT'
	for c in check_u_int:
		if c in value:
			check_type = 'CHECK_U_INT'
	for c in check_bool:
		if c in value:
			check_type = 'CHECK_BOOL'
	for c in check_address:
		if c in value:
			check_type = 'CHECK_ADDRESS'
	return check_type

