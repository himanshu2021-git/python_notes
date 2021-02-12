import requests
import csv
import xlsxwriter as xl

from apiexceptions import *

class CSV:
	def __init__(self,path=None,link=None,sep=","):
		assert path!=None or link!=None,"PATH OR LINK ONE THING IS REQUIRED"
		#LOCAL CSV
		if path:
			try:
				self.data = [x for x in csv.reader(open(path,'r'))]
			except Exception as e:
				raise ReadFailedError(str(e))
		
		elif link:
			try:
				data = str(requests.get(link).content)[2:] 
				text_data = data.replace("\\n","\n").replace("\\t","\t")
				lines_data = text_data.splitlines()
				self.data = [x.split(sep) for x in lines_data]
			except Exception as e:
				raise ReadFailedError(str(e))
		
	def head(self,nrows=5):
		headings = self.data[0]
		print("\t".join(headings))
		print('-'*100)
		for x in self.data[1:nrows+1]:
			print("\t".join(x))
	def tail(self,nrows=5):
		headings = self.data[0]
		print("\t".join(headings))
		print('-'*100)
		for x in self.data[-nrows:]:
			print("\t".join(x))
	
	def replace(self):
		"""
			int,str,float,complex,bool and dictionary are allowed to provide
			if int,str,float,complex,bool provided then replace all the found values.	
			if dict is provided 
				
			{
				'column':[old,new],
				'column1':[old,new]
				....	
			}
		"""
	def groupby(self,base):
		""" 
			a column name is must and that column must contain the elements of which 			frequency is more then one.
			if valid column name is given then you need to return the dictionary 
			
			{
				'1834':[
					[row1],[row1]	
				]
			}
		"""
	def sort(self,column):pass
		
	def typecast(self):
		"""
			perform typecasting according to the data in columns.
		"""
	@classmethod
	def jsontocsv(cls,file):
		"""
			csv of given json.
		"""
	def mean(self):
		"""
			it will return the dictionary which will be having the mean of all numeric 			cols
		"""
	
	def to_csv(self,filename):
		assert filename.endswith(".csv"),"AN ABSOLUTE PATH TO CSV FILE IS REQUIRED"
		file = None
		try:
			file = open(filename,"w",newline="")
		except Exception as e:
			raise WriteFailedError(str(e))
		else:
			writer = csv.writer(file)
			writer.writerows(self.data)
		finally:
			if file:file.close()

	def to_excel(self,filename,sheetname):
		assert filename.endswith(".xlsx"),"AN ABSOLUTE PATH TO EXCEL WORKBOOK IS REQUIRED"
		wb = xl.Workbook(filename)
		
		ws = wb.add_worksheet(sheetname)
		bold = wb.add_format({'bold':True,"underline":True})
		money = wb.add_format({'num_format': '$#,##0.##'})
		headings = self.data[0]
		
		#writing headings
		row = 0
		for col,element in enumerate(headings):
			ws.write(row,col,element,bold)
		
		row += 1
		for r in self.data[1:]:
			for col,element in enumerate(r):
				temp = self.castforexcel(element) 
				if isinstance(temp,float):
					ws.write(row,col,temp,money)
				else:
					ws.write(row,col,temp)
			row += 1
		
		wb.close()
	@staticmethod
	def castforexcel(value):
		value = value.strip()
		if value.isdigit():
			return int(value)
		elif value.replace(".","").isdigit():
			return float(value)
		elif value.startswith('$'):
			if value[1:].replace(".","").isdigit():
				return float(value[1:])
			else:
				return value
		else:
			return value
# GROUP BY ON THE BASIS OF ORDERS AND CREATE A NEW WORKBOOK AND IN THAT WORKBOOK CREATE INDIVIDUAL # SHEETS FOR EVERY SINGLE ORDER

# FIND THE MOST FAMOUS THREE DISHES.

if __name__ == "__main__":
	obj = CSV(link="https://bit.ly/chiporder",sep="\t")
	#obj = CSV()
	#print(obj.data[:5])
	#obj.head()
	#obj.tail()
	#obj.to_csv("newdata.csv")
	obj.to_excel("chiporders.xlsx","orders")
	#print(CSV.castforexcel("$12.5"))
	#print(CSV.castforexcel("12.5"))
	#print(CSV.castforexcel("12"))
	#print(CSV.castforexcel("krishna"))