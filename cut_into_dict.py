def cut_into_dict(sorted_due_instr_list):
	# cut the sorted data into chunk of data in terms of sales name (maybe dictionary?)
	data_dict = {}

	for index3, row3 in sorted_due_instr_list.iterrows():
		if row3['sales'] in data_dict:
			data_dict[row3['sales']] = data_dict[row3['sales']].append(sorted_due_instr_list.loc[[index3]])
			continue
		if type(row3['sales']) == str:
			data_dict[row3['sales']] = sorted_due_instr_list.loc[[index3]]

	#print("List of all NI Sales: ",data_dict.keys())

	print("3. Done cutting the due list into dictionary for each sale")
	return data_dict

if __name__ == '__main__':
	cut_into_dict(sorted_due_instr_list)