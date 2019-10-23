import os, sys, getopt
from openpyxl import load_workbook
from shutil import copyfile

# Load worksheet
def load_worksheet(filename, sheetname):
	wb = load_workbook(filename, data_only=True)
	ws = wb[sheetname]
	return ws

# Find cell boundary
def find_cell(ws, target, match_case=False, find_all=False):
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
								return temp
					if not_merged_cell:
						temp = {'firstcol':cell.column,
								'firstrow':cell.row,
								'lastcol':cell.column,
								'lastrow':cell.row}
						if find_all:
							return_value.append(temp)
						else:
							return temp
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
				return temp
		if not_merged_cell:
			temp = {'firstcol':target[0],
					'firstrow':target[1],
					'lastcol':target[0],
					'lastrow':target[1]}
			return temp

	return return_value

# Get cell value with cell coordinate
def get_cell_value(ws, coor):
	for row in range (coor['firstrow'], coor['lastrow'] + 1):
		for col in range (coor['firstcol'], coor['lastcol'] + 1):
			val = ws.cell(column=col, row=row).value
			if (val != None):
				return val
	#print("Coordinate \'%s\': is blank" %(coor))
	return None

# Shift 'right' cell
def coor_shift_right(ws, coor):
	temp = list([coor['lastcol'] + 1, coor['firstrow']])
	return find_cell(ws, temp)

# Shift 'left' cell
def coor_shift_left(ws, coor):
	col = coor['firstcol'] - 1
	if col < 1:
		col = 1
	temp = list([col, coor['firstrow']])
	return find_cell(ws, temp)

# Shift 'up' cell
def coor_shift_up(ws, coor):
	row = coor['firstrow'] - 1
	if row < 1:
		row = 1
	temp = list([coor['firstcol'], row])
	return find_cell(ws, temp)

# Shift 'down' cell
def coor_shift_down(ws, coor):
	temp = list([coor['firstcol'], coor['lastrow'] + 1])
	return find_cell(ws, temp)

# Get test case row
def row_of_testcase(ws, symbol):
	cur_cell = find_cell(ws, symbol)
	col_of_tc = cur_cell['firstcol']
	first_row_of_tc = cur_cell['lastrow'] + 1
	while (get_cell_value(ws, cur_cell) != None):
		cur_cell = coor_shift_down(ws, cur_cell)
	last_row_of_tc = cur_cell['firstrow'] - 1
	return first_row_of_tc, last_row_of_tc, col_of_tc

def file_write(path, filename, data, position):
	write_done = False
	os.rename(path + filename, 'temp.txt')
	infile = open(path + 'temp.txt', 'r')
	outfile = open(path + filename, 'w')
	for line in infile:
		outfile.write(line)
		if (position in line) and (write_done == False):
			outfile.write(data)
			write_done = True
	infile.close()
	outfile.close()
	os.remove(path + 'temp.txt')

def get_data(ws, target, input_range, tc_row):
	data = ''
	input_cell = coor_shift_down(ws, input_range)
	while input_cell['lastcol'] <= input_range['lastcol']:
		# Check [a]
		cur_input_param = get_cell_value(ws, find_cell(ws, [input_cell['firstcol'], tc_row]))
		if (target in get_cell_value(ws, input_cell)):
			data = data + cur_input_param + ', '
		input_cell = coor_shift_right(ws, input_cell)
	return data

def is_file_created(dir, file):
	check_dir = ".\\" + str(file) 
	if (os.path.isfile(check_dir)):
		f = open('%s' % file, 'a')
	else:
		f = open('%s' % file, 'w')
	return f

# Main function
def main(argv):
	check_sequence = False
	try:
		opts, args = getopt.getopt(argv,"hid:i:ws:se:",["idir=","ifile=","wsheet=","check_seq"])
	except getopt.GetoptError:
		print("test.py --idir <inputfir> --ifile <inputfile> --wsheet <worksheet> --check_seq <True/False>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("test.py --idir <inputfir> --ifile <inputfile> --wsheet <worksheet>")
			sys.exit()
		elif opt in ("-id", "--idir"):
			inputdir = arg
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-ws", "--wsheet"):
			worksheet = arg
		elif opt in ("-se", "--check_seq"):
			check_sequence = arg

	# Get working sheet
	ws = load_worksheet(inputdir + '\\' + inputfile, worksheet)
	# Get Test case start row and end row
	tc_sta_row, tc_end_row, tc_col = row_of_testcase(ws, '#')
	# Get Input factor range
	input_factor = find_cell(ws, 'Input factor')
	# Get Output element range
	output_element = find_cell(ws, 'Output element')

	# Create file .h
	dot_h = open('test_' + worksheet + '.h', 'w')
	# Begin of file
	data = 'struct CPPTH_LOOP_INPUT_STRUCT CPPTH_LOOP_INPUT[] = {\n'
	dot_h.write(data)
	# Add test case
	# Input factor
	for tc_row in range(tc_sta_row, tc_end_row + 1):
		# Reset data
		data = '\t{'
		# Add test case number to data
		tc_num = get_cell_value(ws, find_cell(ws, [tc_col, tc_row]))
		data = data + '\"' + tc_num + '\"' + ', '
		
		# Add description to data
		describe = find_cell(ws, 'Item')
		data = data + '\"' + get_cell_value(ws, find_cell(ws, [describe['firstcol'], tc_row])) + '\"' + ', '
		del describe
		
		# Add expected calls sequence
		# In case not check sequence of calling stub function
		input_cell = coor_shift_down(ws, input_factor)
		if (check_sequence == False):
			data = data + '"{'

			while input_cell['lastcol'] <= input_factor['lastcol']:
				# Check [rt] symbol for getting function name
				cur_func = get_cell_value(ws, input_cell)
				if ('[rt]' in cur_func):
					data = data + '{' + cur_func[cur_func.find(' ') + 1 : cur_func.find('(')] + '#' + tc_num + '}'
				input_cell = coor_shift_right(ws, input_cell)
			
			data = data + '}"' + ', '

		else:
			data = data + '"{'

			while input_cell['lastcol'] <= input_factor['lastcol']:
				# Check [rt] symbol for getting function name
				cur_func = get_cell_value(ws, input_cell)
				if ('[rt]' in cur_func):
					data = data  + cur_func[cur_func.find(' ') + 1 : cur_func.find('(')] + '#' + tc_num + ';'
				input_cell = coor_shift_right(ws, input_cell)
			
			data = data[:-1] + '}"' + ', '
		del input_cell, cur_func

		# Add execute
		data = data + '1' + ', '

		# Add input param
		data = data + get_data(ws, '[a]', input_factor, tc_row)

		# Add global variable
		data = data + get_data(ws, '[g]', input_factor, tc_row)

		# Add expected global variable
		data = data + get_data(ws, '[g]', output_element, tc_row)

		# Add test result
		data = data + get_data(ws, 'Return value', output_element, tc_row)

		# Write to file
		data = data[:-2] + '},\n'
		dot_h.write(data)

	# End of file
	data = '};\n'
	dot_h.write(data)
	dot_h.close()

if __name__ == "__main__":
	main(sys.argv[1:])
