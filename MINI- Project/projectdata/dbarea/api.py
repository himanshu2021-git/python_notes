from sqlite3 import connect
from . import query as qry
class MySql:
    def __init__(self,**kwargs):
        try:
            self.conn = connect(kwargs.get("database"))
            self.cur = self.conn.cursor()
        except Exception as e:
            raise TypeError(f"{e}")
    
    def createTable(self,table_name):
        self.table = table_name
        try:
            self.cur.execute(
                qry.create_table.format_map(
                    dict(
                        table_name=table_name
                    )
                )
            )
        except Exception as e:
            self.conn.rollback()
            raise TypeError(f"{e}")
        else:
            self.conn.commit()
            return True

    def insertData(self,**kwargs):
        try:
            self.cur.execute(
                qry.insert_data.format_map(
                    dict(
                        table_name = self.table,
                        id = kwargs.get("id"),
                        product_name = kwargs.get("product_name"),
                        price = kwargs.get("price"),
                        in_stock = kwargs.get("in_stock"),
                        barcode_no = kwargs.get("barcode_no"),
                        barcode = kwargs.get("barcode")
                    )
                )
            )
        except Exception as e:
            self.conn.rollback()
            raise TypeError(f"{e}")
        else:
            self.conn.commit()
            return True
        
    def readData(self,**kwargs):
        try:
            self.cur.execute(
                qry.read_data.format_map(
                    dict(
                        table_name=self.table,
                        product_id = kwargs.get("product_id")
                    )
                )
            )
        except Exception as e:
            raise TypeError(f"{e}")
        else:
            return self.cur.fetchall()
    
    def __del__(self):
        try:
            if self.cur:self.cur.close()
            if self.conn:self.conn.close()
        except Exception as e:
            raise TypeError(f"{e}")