from common import load_worksheet
from sample import test_part

filename = '.\\old\\sample.xlsx'
sheetname = 'file_name_2'
ws = load_worksheet(filename, sheetname)
print(ws)
print(test_part(ws, sheetname))
