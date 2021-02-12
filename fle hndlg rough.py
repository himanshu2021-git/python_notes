#File handling...and its operation
#python support file handling...basically in python data will be store in temporary storage
#here we handle text file or binary file
#heap allocate us to temporary stograge.

#permission in file handling
#Open a file
#before performing any operation first open the file
#for these we should use python inbuilt function called open() function but at the time of open any file we have to provide specific mode.
#e.x... f=open("nishant.txt","r")

#MODES--
# r-> open an exisiting file for read operation.The file pointer is in postion at the starting(begining) of the file.File pointer is invisible.
# w--> open an existing file for write operation.if file contain some data previously then it will override. like if i opened A file named as himansu.txt and now i want to create a file inside it which name will be raj.txt but if there will be a exisiting file which has same name then the new creating file will override it.
# a--> open an exisiting file for append operation.It won't override existing data.
# r+ --> to read and write into the file.The previous data in the file will not be deleted. the file pointer is placed at the begining of the file.
# w+ -->first write then read file.
# a+ --> to append and read the data.It would overriden.
# x --> exclusive mode. if the file open with exclusive mode,if that file already exist then we will get file exist error
