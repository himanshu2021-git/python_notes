from dbarea.api import MySql

db = MySql(
    database="storagearea/inventorydb.db"
)
db.createTable("products_data")