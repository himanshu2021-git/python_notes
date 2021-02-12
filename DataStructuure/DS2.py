#CSV = comma separated values.It is same as text file you can only store string data in it.
#predefined module=import csv
"""import csv
file=open("ex1.csv",'r')
data=csv.reader(file)
print(file.tell())
result=[x for x in data]
print(result[:10])
print(file.seek(0))
data=csv.DictReader(file)
result=[x for x in data]
print(result[:10])
"""



#CREATING OWN APIs

import requests
import csv
from excepti import *

class CSV:
    def __init__(self,path=None,link=None):
        assert path!=None or link!=None,"PATH OR LINK ONE THING IS REQUIRED"
        #Local CSV
        if path:
            try:
                self.data=[x for x in csv.reader(open(path,'r'))]
            except Exception as e:
                raise RaisedFailedError(str(e))
        elif link:
            try:
                text_data =str(request.get(link).content)[2:].replace("\\n","\n")
                print(text_data)
            except Exception as e:
                raise ReadFailedError(str(e))

if __name__=="__main__":
    obj=CSV(link="https://bit.ly/uforeports")
