#PDBC: Python DATABASE CONNECTIVITY
#we can connect db using file system butits not secure and not in a proper way

#LOCAL DB: IT behaves like a file.it stores like a file but daata store inside this is highly secure.it has own algos.no virus can ttack.file may be cracked or delte it stores on hardware
#CLOUD DB:  it stores at server use when we need to push data automatically to users

#LOCAL DB USE: store data on device.

#Cursor:represent the current location.blinking


#----------------------STEPS TO COMMUNCICATE OF ANY TYPE OF DB

#1-KEEP UR DB READY AND INACTIVE STATE.
#----local--create the local db file,cloud:keeo server running

#2: install the database specific module.
#-----local--no installtion required----import sqlite3

#-----mysql---pip install pymysql(it might fail) or pip install mysql-connector #recommended
#from mysql.connector import connect
#fro, pymysql import connect


#----------oracle---pip install cx_Oracle---from cx_Oracle import connect

#3: create connection----have to find pATH----
#local----conn=connect("absolute path to your db file WITH extension")

#cloud----- mysql case->
"""conn=connect(
    host="db host"
    port="ur port"
    user="user name"
    password="password"
    db="name of your db"

)"""

#ORACLE CASE
"""
conn=connect(
    "host:port@user:password/db"
    )
"""

#PYTHON is connected with DATABASE::::::::::::::::

#4:create the cursor:
#----same in all local server or oracle sql
"cur=conn.cursor()"


#5:exectuing the query:

"""cur.execute(qry)
cur.executemany(qry,param)
"""

#6:::if in the 5th step create,update or delete operation was performed then you will have to commit the changes

"conn.commit()"

#7::::if something goes wrong during 5th or 6th step then you can call rollback method to recover the last known state of your db
"conn.rollback()"


#8:if reAD OPERATION was performed in 5th step then unpack the result
"""cur.fetchone()#get you single row
cur.fetchmany(n)#return n rows
cur.fetchall()#return all the rows
"""


#9:close the cursor:::::
"cur.close()"

#10:::close the connection:
"conn.close()"




#local----------------------------------------


#KEEP DB READY----
#install db model---- alredy done
#CREATE CONNECTION---


import sqlite3 as sq
from random import randint,choice
data=[[choice(list("ABCDEFGHI")),choice(list("ABCDEFGHI")),]for x in range(20)]
try:
    conn=sq.connect("mydatabase.db")
    cur=conn.cursor()#creating cursor
    
except Exception as e:
    print(e)
else:
    print("Connection and cursor Created")
    #performing create operation
    try:
        #cur.execute("""
        #CREATE TABLE IF NOT EXISTS PERSONS(
        #first_name text,
        #last_name text,
        #age number
        #)
    #""")
        #inserting data into tabLE
        #for first,last,age in data:
        #    cur.execute("""
          # first_name,
           # last_name,
            #age
           # )VALUES(
            #    '{first}',
             #   '{last}',
              #  {45}
            #""")
        
        #conn.commit() #commiting the create operation
    #reading fromdatabase
              cur.execute("SELECT * FROM PERSONS")
        
    except Exception as e:
        conn.rollback()
    else:
        print("Table Created")
        print("DATA Inserted")
        #UNOACKING THE DATA
        print(cur.fetchone())
        print(cur.fetchmany(3))
        print(cur.fetchall())
finally:
    if cur:
        cur.close() #closing cursor
        print("cursor close")
    if conn:
        conn.close()#closung connection
        print("connection closed")





























