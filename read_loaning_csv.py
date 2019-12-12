import pandas as pd
import math
import datetime
import xlrd

def read_loaning_csv():
	nan = float("nan")

	#1. read only the 到期日 column
	due_date_col = pd.read_csv("測試內部財產.csv",header=None ,names=['date'], usecols=[11], lineterminator='\n', index_col=False, encoding = "big5hkscs")
	
	#2. loop all entry in due_col to retrieve the index of all rows that are due
	skip_row_index = []
	for index, row in due_date_col.iterrows(): 		
		if type(row['date']) == type(nan):
			skip_row_index.append(index)
			#print(index,row['date'],type(row['date']),"it's a float")
				
	#3. retrieve all rows that are really due
	due_instr_col = ['model','sn', 'customer', 'loaning_sn', 'sales', 'loaning_date' , 'due_date']
	due_instr_list = pd.read_csv("測試內部財產.csv",header=None, names=due_instr_col,usecols=[1,2,7,8,9,10,11],skiprows=skip_row_index,lineterminator='\n',encoding = "big5hkscs")
		
	#4. sort the data
	sorted_due_instr_list = due_instr_list.sort_values(by='sales')

	#print(sorted_due_instr_list)
	print("1. Done reading the 內部財產.csv file")
	return sorted_due_instr_list


if __name__ == '__main__':
	read_loaning_csv()