import sys
import numpy as np
import smtplib
import pandas as pd
from send_email import send_email
from read_loaning_csv import read_loaning_csv
from cut_into_dict import cut_into_dict
from read_sales_csv import read_sales_csv
from check_due_date import check_due_date

# 1. read loaning csv:
#		input: csv
#		output: raw data numpy array
sorted_due_instr_list = read_loaning_csv()

# 2-1. check due day
#		input: raw data numpy array
#		output: overtimed sorted numpy array, about to due within 7 days 
sorted_due_instr_list = check_due_date(sorted_due_instr_list)

# 2-2. cut the list into chunk of data
data_dict = cut_into_dict(sorted_due_instr_list)

# 3. read sales csv:
#		input: csv
#		output: sorted sales numpy array
sorted_sales_list = read_sales_csv()

#4.  loop:
#		read 1 row in sorted sales numpy array 
#		read the corresponding section of overtimed, sorted numpy array
#		send the email
for index, row in sorted_sales_list.iterrows(): 	
	print("Dealing with sales:",row['sales'])
	title = row['sales']
	try:
		context = data_dict[row['sales']]
	except KeyError as e:
		print("No ",row['sales'],"\' data: ", e)
		continue
	#send_email('welly.huang@ni.com',[row['sales_email'],row['sales_manager_email1'],'welly.huang@ni.com'],title,context)
	send_email('welly.huang@ni.com','welly.huang@ni.com',title,context)