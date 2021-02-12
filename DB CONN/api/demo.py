from dbapi import Database
from random import randint,choice
f = "sonu monu manoj krishna mahesh ankit samarth".split()
l = "sharma verma singh kapoor chadhdha".split()
data = [[choice(f),choice(l),randint(20,45)] for x in range(10)]
# ------LOCAL---------
# user = Database(
#     dbkind="local",
#     dbpath="mydb.db",
#     dbmodule="sqlite3",
#     querymodule = "query"
# )

#-------SERVER----------
user = Database(
    dbkind="server",
    dbmodule="mysql.connector",
    querymodule="query",
    host = "remotemysql.com",
    port=3306,
    database="kmeSJcz0Au",
    user="kmeSJcz0Au",
    password="kvLG2YdVXv",
)

#user.info()

print('TABLE CREATED') if user.createtable() else print('TABLE NOT CREATED')

#print('DATA INSERTED') if user.insertdata(data) else print('DATA NOT INSERTED')

print(user.readdata(5))