#Permanent Data Structures-----------------------------------------
#dats structure is use for inifinity amount of data and variable use for n amunt of data.#It has two types
#-file system,-

#buffering-gathering information from resource. /

#IO buffer object- any python object which is connected with the outer resource.

#we have a python function which helps you to create IO buffer ibject
#open("abs. file path to some file","mode") -> IO biffer

#mode for text only
#--------------------
#r--- open a file for reading only and if file not fount then FileNotFoundError will be raised
#w-for write and if not present and new file will be created and write operation will be allowed to perform with that io buffer object.
#a-opens a file file for appendation only if that file is not present at given location then a new file will be created and write operation will be allowed to perform but if file is [resent then append operation(no oroginal data will be lost)will be allowed  to be performed
#r+---firstly read then write if file not found then error
#w+--first write then read
#a+--first apppend then read

#x--exclusive mode |opens a file for writing if that file is not present then only but if file is present at given location then FileExistsError will be raised. NO OVERRIDE OPERATION PERFORM LIKE w.
#----This mode is specially used to create the file


#BASIC METHODS AND ATTRBUTES OF AN IO BUFFER OBJECT
"""
file =None
try:
    file=open("que.txt","r")
except FileNotFoundError as e:
    print(e)
else:
    print("File opened succesfully")
    print(file.name)
    print(file.mode)
    print(file.readable())
    print(file.writable())
    print(file.closed)
finally:
    if file:
        file.close() #will close fully
print("Is file closed now",file.closed)

"""
#REading a text file--------------------------
#file.tell()---return the postion of cursor

#file.seek(n)---changes the postion of cursor
#file.read(n)---reads n character from current of postion of cursor
#file.readline()----read till \n
#file.readlines()----reads entire file and returns a list of strings where each string represnts single line


"""
file =None
try:
    file=open("que.txt","r")
except FileNotFoundError as e:
    print(e)
else:
    if file.readable():
        print(f'CURRENT:{file.tell()!r}')
        print(file.read(10))
        print(f'CURRENT :{file.tell()!r}')
        print(f'UPDATED POSiTION :{file.seek(5)!r}')
        print(file.readline())
        print(file.readline())
        print(file.readlines())
finally:
    if file:
        file.close() #will close fully
print("Is file closed now",file.closed)

"""


#WRITING A TEXT FILE

file =None
try:
    file=open("que1.txt","w")
except FileNotFoundError as e:
    print(e)
else:
    if file.writable():
        file.write("blah blajj blaj blaah b;ahh\n") #can write only one line
        file.writelines("blah blajj blaj blaah b;ahh\n".split()) # can write multiple lines        
finally:
    if file:
        file.close() #will close fully

#Task: define a function called stats_of_file this function is going to have an absolute path a text file.
#lines: words,spaces:paragraphs page has only permit to enter 25 lines alphabets,special symbols numericals data

















