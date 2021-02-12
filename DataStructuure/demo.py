import requests
import csv

# LOADING THE DATA FROM LINK
def loaddata(url):
	data = requests.get(url).text
	data = data.splitlines()
	return [x.split(',') for x in data]

data = loaddata("https://bit.ly/drinksbycountry")

def checkcolumnname(func):
	def inner(*args,**kwargs):
		if args[1] in args[0][0]:
			return func(*args,**kwargs)
		else:
			print('INVALID COLUMN NAME')
			return False
	return inner

def checkfrequency(func):
	def inner(*args,**kwargs):
		column_index = args[0][0].index(args[1])
		column_data = [element[column_index] for element in args[0][1:]]
		#print(column_data)
		if len(set(column_data)) != len(column_data):
			return func(*args,**kwargs)
		else:
			print('GROUP BY OPERATION NOT POSSIBLE WITH THIS COLUMN.')
			return False
	return inner

@checkcolumnname
def mean(data,column_name):
	#1 extract the column data
	headings = data[0]
	column_index = headings.index(column_name)
	column_data = [row[column_index] for row in data[1:]]
	
	#2 check the given column contains only numerics
	for x in column_data:
		if not (x.isdigit() or x.replace(".","").isdigit()):
			break
	else:
		#3 type cast the data
		type_casted_data = [float(x) for x in column_data]
		return (sum(type_casted_data)/len(type_casted_data))
	
	print('COLUMN DOES NOT CONTAIN ONLY NUMERIC DATA')
	return False

@checkcolumnname	
def count(data,column_name):
	#1 extract the column data
	headings = data[0]
	column_index = headings.index(column_name)
	column_data = [row[column_index] for row in data[1:]]
	
	#find unique elements out of column data
	unique_elements = set(column_data)

	return {element:column_data.count(element) for element in unique_elements}


@checkcolumnname
@checkfrequency
def groupby(data,column_name):
	#1 extract the column data
	headings = data[0]
	column_index = headings.index(column_name)
	column_data = [row[column_index] for row in data[1:]]
	
	#2 unique elements
	unique_elements = set(column_data)
	
	#3 iterate over the collection and look for element in given column name.
	return {
		each:[
			row for row in data[1:] if row[column_index] == each
		] for each in unique_elements
	}

def replace(data,old,new,all=True,default_old=None,default_new=None):
	temp = False
	# if old and new are of str,int,float,bool or complex type then replace entire stuff
	if isinstance(old,(int,str,float,bool,complex)) and isinstance(new,(int,str,float,bool,complex)):
		row = 1
		while row < len(data):
			col = 0
			while col < len(data[row]):
				if data[row][col] == old:
					data[row][col] = new
					if not all:
						temp = True
						break
				col += 1
			if temp:
				break
			row += 1
					
	elif isinstance(old,dict) and isinstance(new,dict):
		#checking that columns names are valid or not
		if len(old) == len(new):
			for old_k,new_k in zip(old.keys(),new.keys()):
				if old_k not in data[0] or new_k not in data[0]:
					break
			else:
				old_index = {data[0].index(x):x for x in old}
				row = 1
				while row < len(data):
					col = 0
					while col < len(data[row]):
						if data[row][col] == old.get(old_index.get(col),default_old):
							data[row][col] = new.get(old_index.get(col),default_new)
							if not all:
								temp = True
								break
						col += 1
					if temp:
						break
					row += 1
				return True
			print("SOME COLUMN NAME IS INVALID.")
			return False 
			
	else:
		print('INVALID ARGUMENTS PROVIDED')
		return False

	
replace(data,old={
	'country':'India',
	'continent':'Asia'
},new={
	'country':"India".center(50,"*"),
	'continent':'Asia'.center(50,"-")
},all=True)

print(data)	

	

