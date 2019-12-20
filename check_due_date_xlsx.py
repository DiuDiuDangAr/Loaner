import datetime

def check_due_date_xlsx(sorted_due_instr_list):
	now_d = datetime.datetime.today()

	for index, row in sorted_due_instr_list.iterrows():
		try:
			if ((now_d-row['due_date']).days) < 0:
				#not due => drop it
				sorted_due_instr_list = sorted_due_instr_list.drop([index])
		except:
			sorted_due_instr_list = sorted_due_instr_list.drop([index])

	#print(sorted_due_instr_list)
	print("2. Done filter the due items")
	return sorted_due_instr_list