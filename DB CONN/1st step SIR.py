"""PYTHON DATABASE CONNECTIVITY - PDBC

steps to communicate with any type of database

1- keep your database ready and in active state.
	local - create the local db file
	cloud database - keep server running.

2- install the database specific module.
	local - no installation is required - import sqlite3
	mysql - pip install pymysql or pip install mysql-connector # recommended 
		from mysql.connector import connect
		from pymysql import connect
	oracle - pip install cx_oracle - from cx_Oracle import connect

3- create connection
	local
		conn = connect("absolute path to your db file with extension")
	cloud	
		MYSQL
		conn = connect(
			host = "your db host",
			port = your port,
			user = "your user name",
			password = "your password",
			db = "name of your db"
		)
		ORACLE
		conn = connect(
			"host:port@user:password/db"
			
		)

4- create the cursor
	cur = conn.cursor()

5- executing the query
	cur.execute(qry)
	cur.executemany(qry,param)

6- if in the 5th step create,update or delete operation was performed then you will have to commit the    changes
	conn.commit()

7- if something goes wrong during 5th or 6th step then you can call rollback method to recover the    last known state of your database
	conn.rollback()

8- if read operation was performed in 5th step then unpack the result
	cur.fetchone() # get you single row
	cur.fetchmany(n) # get you n rows
	cur.fetchall() # return all the rows

9- close the cursor
	cur.close()

10 close the connection
	conn.close()
"""

#---------------------------------------------------
# KEEP DB READY
# INSTALL DB MODULE
import sqlite3 as sq
from random import randint,choice
# created dummy data to be inserted into the table.
data = [[choice(list("ABCDEFGHI")),choice(list("ABCDEFGHI")),randint(20,30)] for x in range(20)]

conn = None
cur = None
try:
	conn = sq.connect("mydatabase.db") # CREATE CONNECTION
	cur = conn.cursor() # CREATE CURSOR
except Exception as e:
	print(e)
else:
	print('CONNECTION & CURSOR CREATED')
	# performing create opration
	try:
		#cur.execute("""
		#	CREATE TABLE IF NOT EXISTS PERSONS(
		#		first_name text,
		#		last_name text,
		#		age number	
		#	)
		#""")
			
		# inserting data into table
		#for first,last,age in data:
		#	cur.execute(f"""
		#		INSERT INTO PERSONS(
		#			first_name,
		#			last_name,
		#			age
		#		)VALUES(
		#			'{first}',
		#			'{last}',
		#			{age}
		#		)
		#	""")
		#conn.commit() # commanding database to reflect the changes into it
		
		# reading from database
		cur.execute("SELECT * FROM PERSONS")
	except Exception as e:
		# recover the database to lastly known state
		conn.rollback()
		print(e)
	else:
		#print('TABLE CREATED')
		#print('DATA INSERTED')
		#UNPACKING THE DATA
		print(cur.fetchone())
		print("--------------------")
		print(cur.fetchmany(3))
		print("-------------------")
		print(cur.fetchall())
finally:
	if cur:
		cur.close() # closing the cursor
	if conn:
		conn.close() # closing the connection	
