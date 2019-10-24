import os, sys, getopt
from openpyxl import load_workbook
from shutil import copyfile
import shutil

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

# Append text to file
def file_write(path, filename, data, position):
	write_done = False
	count = 0
	os.rename(path + filename, path + 'temp.txt')
	infile = open(path + 'temp.txt', 'r')
	outfile = open(path + filename, 'w')
	for line in infile:
		outfile.write(line)

		try:
			if (position[count] in line):
				count += 1
		except:
			pass

		if (count == len(position)) and (write_done == False):
			outfile.write(data)
			write_done = True

	infile.close()
	outfile.close()
	os.remove(path + 'temp.txt')

# Extract data from PCL with specific target
def get_data(ws, target, input_range, cur_row):
	data = ''
	input_cell = coor_shift_down(ws, input_range)
	while input_cell['lastcol'] <= input_range['lastcol']:
		# Check input cell merged rang, if merge range use {var1, var2}
		if (target in get_cell_value(ws, input_cell)):
			if (input_cell['lastcol'] - input_cell['firstcol']) == 0:
				cur_input_param = get_cell_value(ws, find_cell(ws, [input_cell['firstcol'], cur_row]))
				data = data + cur_input_param + ', '
			else:
				data = data + '{'
				element_cell = coor_shift_down(ws, input_cell)
				while element_cell['lastcol'] <= input_cell['lastcol']:
					cur_input_param = get_cell_value(ws, find_cell(ws, [element_cell['firstcol'], cur_row]))
					data = data + cur_input_param + ', '
					element_cell = coor_shift_right(ws, element_cell)
				data = data[:-2] + '}, '

		input_cell = coor_shift_right(ws, input_cell)
	return data

# Check if file is created or not, and use attribute to open file
def is_file_created(dir, file):
	check_dir = ".\\" + str(file)
	if (os.path.isfile(check_dir)):
		f = open('%s' % file, 'a')
	else:
		f = open('%s' % file, 'w')
	return f

# Create file .h contrain test case
def create_test_case_file(ws, worksheet, check_sequence=False):
	# Get Test case start row and end row
	start_row, end_row, testcase_col = row_of_testcase(ws, '#')
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
	for cur_row in range(start_row, end_row + 1):
		# Reset data
		data = '\t{'
		# Add test case number to data
		tc_num = get_cell_value(ws, find_cell(ws, [testcase_col, cur_row]))
		data = data + '\"' + tc_num + '\"' + ', '

		# Add description to data - Named: Item
		describe = find_cell(ws, 'Item')
		data = data + '\"' + get_cell_value(ws, find_cell(ws, [describe['firstcol'], cur_row])) + '\"' + ', '
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

		# Add execute - 1: execute this function
		data = data + '1' + ', '

		# Add input param by detect [a]
		# TODO: Add detect structure - DONE

		data = data + get_data(ws, '[a]', input_factor, cur_row)

		# Add global variable by detect [g]
		data = data + get_data(ws, '[g]', input_factor, cur_row)

		# Add expected global variable by detect [g] in output element
		data = data + get_data(ws, '[g]', output_element, cur_row)

		# Add test result by detect 'Return value' in output element
		data = data + get_data(ws, 'Return value', output_element, cur_row)

		# Write all the data to file
		data = data[:-2] + '},\n'
		dot_h.write(data)

	# End of file
	data = '};\n'
	dot_h.write(data)
	dot_h.close()
	del dot_h

#
def create_stub_file(ws, worksheet, src_dir, src):
	# Create stub function
	dot_c = open('test_' + worksheet + '.c', 'w')
	start_row, end_row, testcase_col = row_of_testcase(ws, '#')
	# Get Input factor range
	input_factor = find_cell(ws, 'Input factor')
	# Get Output element range
	output_element = find_cell(ws, 'Output element')

	for cur_row in range(start_row, end_row + 1):
		# Get test case number
		tc_num = get_cell_value(ws, find_cell(ws, [testcase_col, cur_row]))
		# Create instance for test case num

		input_cell = coor_shift_down(ws, input_factor)
		while input_cell['lastcol'] <= input_factor['lastcol']:
			# Check [rt]
			cur_input_param = get_cell_value(ws, find_cell(ws, [input_cell['firstcol'], cur_row]))

			if ('[rt]' in get_cell_value(ws, input_cell)):
				# Get function name
				func_name = get_cell_value(ws, input_cell)
				# Extract function name from [rt]type function_name(...);
				func_name = func_name[func_name.find(' ') + 1: func_name.find('(')]
				# TODO: title is Isolate, need to implement for other title, Stub, Wrapper
				title = '/* Isolate for function %s */\n' %(func_name)
				# Set instance
				if_instance = '\tIF_INSTANCE(\"%s\") {\n' %(tc_num)
				outval_data = ''

				check_data = ''
				output_cell = coor_shift_down(ws, output_element) 
				while output_cell['lastcol'] <= output_element['lastcol']:
					# Check [f] symbol and check the function name
					if ('[f]' in get_cell_value(ws, output_cell)) and (func_name in get_cell_value(ws, output_cell)):
						check_point = coor_shift_down(ws, output_cell)
						while check_point['lastcol'] <= output_cell['lastcol']:
							# TODO: add replace 'CHECK_S_INT'
							check_point_val = get_cell_value(ws, find_cell(ws, [check_point['firstcol'] , cur_row]))
							if (check_point_val != None) and (check_point_val) != '-':
								check_data = check_data + '\t\t' + 'CHECK_S_INT' + '(' + get_cell_value(ws, check_point) + ', ' + check_point_val + ');\n'

							check_point = coor_shift_right(ws, check_point)
					output_cell = coor_shift_right(ws, output_cell)

				# Function output value
				if input_cell['lastcol'] < input_factor['lastcol']:
					outval_range = coor_shift_right(ws, input_cell)
					if ('[f]' in get_cell_value(ws, outval_range)):
						outval_cell = coor_shift_down(ws, outval_range)
						while outval_cell['lastcol'] <= outval_range['lastcol']:
							outval = get_cell_value(ws, find_cell(ws, [outval_cell['firstcol'], cur_row]))
							if (outval != None) and (outval != '-'):
								outval_data = outval_data + '\t\t' + '*' + get_cell_value(ws, outval_cell) + ' = ' \
								+ outval + ';\n'
							outval_cell = coor_shift_right(ws, outval_cell)

				data_return = '\t\treturn ' + get_cell_value(ws, find_cell(ws, [input_cell['firstcol'], cur_row])) + ';\n\t}\n'
				data = if_instance + check_data + outval_data + data_return

				# Get position for append data to source
				position = [title, 'IF_INSTANCE("default")', '}']
				# Write file to test program of Cantata
				file_write(src_dir, 'test_' + src + '.c', data, position)

				data = title + data
				dot_c.write(data)

			input_cell = coor_shift_right(ws, input_cell)
	dot_c.close()


# Main function
def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hid:i:ws:sr:se:ca:",["idir=","ifile=","wsheet=","source=","check_seq=","can_dir="])
	except getopt.GetoptError:
		print("--idir <inputfir> --ifile <inputfile> --wsheet <worksheet> --check_seq <True/False> --source <source>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("--idir <inputfir> --ifile <inputfile> --wsheet <worksheet>")
			sys.exit()
		elif opt in ("-id", "--idir"):
			inputdir = arg
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-ws", "--wsheet"):
			worksheet = arg
		elif opt in ("-sr", "--source"):
			source = arg
		elif opt in ("-se", "--check_seq"):
			check_sequence = arg
		elif opt in ("-ca", "--can_dir"):
			src_dir = arg + '\\'

	# Get working sheet
	ws = load_worksheet(inputdir + '\\' + inputfile, worksheet)

	# Create file dot h, contain all the test case
	create_test_case_file(ws, worksheet, check_sequence)

	src_dir = src_dir + 'test_' + source + '\\'
	create_stub_file(ws, worksheet, src_dir, source)

if __name__ == "__main__":
	main(sys.argv[1:])
