import datetime

def check_due_date(sorted_due_instr_list):
	now_d = datetime.datetime.today()

	for index, row in sorted_due_instr_list.iterrows():
		try:
			loan_d_list = row['due_date'].split('/')
			loan_d = datetime.datetime(int(loan_d_list[0]),int(loan_d_list[1]),int(loan_d_list[2]))
			if ((now_d-loan_d).days) < 0:
				#not due => drop it
				sorted_due_instr_list = sorted_due_instr_list.drop([index])
		except:
			sorted_due_instr_list = sorted_due_instr_list.drop([index])

	#print(sorted_due_instr_list)
	print("2. Done filter the due items")
	return sorted_due_instr_list