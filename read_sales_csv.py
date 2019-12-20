import numpy as np
import pandas as pd

def read_sales_csv():
	
	col = ['sales','sales_email', 'sales_manager_email1', 'sales_manager_email2', 'not_used', 'sales_name']
	sales_email_list = pd.read_csv("email vs loaner.csv",header=None, names=col)
	sorted_sales_email_list = sales_email_list.sort_values(by='sales')
	
	print("4. Done reading the sales list (emails)")
	return sorted_sales_email_list

if __name__ == '__main__':
		read_sales_csv()