#MODULE PROGRAMMING..........
#--------------------------------
#each and every python saved file is called python module, but they aren't proper module.beacause module programming has a structure.

#--------------------------\ this used as removing functionLITY

#PCKAGES>>>>>>>>>>>>>>>>>>>>>
#-------------------------------------
#package is a folder in which various python modules are placed.
#python always convert module into low level language. found in __pycache__

#1. BUILT-IN PACKAGES MODULE | PREDEFINE | LIBRARY MODULE OR PACKAGES.
#--------THESE modules or packages are comes with standard python installation you can just bring them to you code and use them

#2. Third party packages and module
#----these module or packages are laso alredy defined but not avaialable locally into you system before using them you will have to install them.

#3.USER DEFINED PACKAGES AND MODULE.
#__________these pkgs and modules are defined by us.

#python stuff required to deal with packages and modules
#_-----------------------------------

#from,import,as,(),.(dot operator)

#from......import.....
#--------these keyword is used to import something specific from a packages or a module.

#from random import(randint as ri,choice as ch, shuffle as sh)




#IMPORT
#--------------this keyword use to import entire stuff

#as
#----this keyword is used as aliasing | renaming the thing during import operation

#every module has a documentation string inside it """  """ inside this and they stored in __doc__
"""
if __name__ == "__main__":
    main() #function name........execute only when you try to execute these module direclty if we import the file then the code is not seen"""




# BUILT-IN MODULE-------------------------------------------------------
#OS MODULE- THIS module  helps you to perform the task which you usually do with windows

#os.getcwd---retur  the current working directory

#os.mkdir---absolute path+folder name give then create folder at given location

#os.rmdir---abs.path+filder name give remove the directory

#os.system---any command of dos----allows you to execute any command of dos| command prompt

#os.startfile______-- absolute path to executable file

"""import os
os.getcwd
"""

#----------------------------------------- Next class--------------------------------

#regular expression---------- re are used to find a pattern in string. re can only be appplied only in string pattern

#SYMBOLS OF RE
#-- abc - abc exact same and one time only.
#[abc]-- a or b or c wother one of find then re matched.
# re is used alot to find syntax error
#[a-z] -- a to z
#[A-Z] -- A to Z
#[0-9]-- all the digits
#[^abc]-- everything except a or b or c
#[^a-zA-Z0-9](there is no comma and space while giving more than one re)--all symbols match only.

#CHARACTER CLASS--
#\d -- digits
#\D -- excepts digit
#s-- space
#S-- except space
#c-- alphanumeric
#C-- except alphanumeric


#SPECIAL SYMBOL ALSO
#^abc -- starts with abc
#abc$-- ends with abc
#()--partitions of re
#\-- functionality remover
#. -- all characters match no symbols

#QUANTIFIER-----
#a ---- a exact one time
#a? --- a exact one time or zero time
#a+ --- a any number of time but atleast once
#a* -- anny number of time may be zero too
#a{n}--- a exactly n time
#a{n,m}-- a exactly min n time and maximum m time


#1- REGEX to match a string that must start with "A" and must end with"."
"""import re
regex ="^A.*Z$"

data="A bcdsdcsdnk Z"
find = re.search(regex,data)
if find:
    print('pattern matched')
    print('starting position is',find.start())
    print('the string is',find.string)
else:
    print("string isn;t according to method")


#mmostly re is used in web scraping
"""
"""regex ="<td[a-zA-Z0-9 =\">\n/,\[]]+</td>"
find = re.findall(regex,data)
"""
import re

reg="[a-zA-Z0-9]+@[a-zA-Z].[a-zA-Z]{2,5}"
data="himmupurohit1998@gmail.com"
find=re.search(reg,data)
if find:
    print("Pattern matched")
else:
    print("string is wrong")

