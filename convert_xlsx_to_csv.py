import pandas as pd

def convert_xlsx_to_csv():
	df = pd.read_excel("內部財產.xlsx")
	df.to_csv("內部財產複本.csv", sep=",", encoding="big5hkscs")
	print("test")
	#okok

if __name__ == '__main__':
	convert_xlsx_to_csv()