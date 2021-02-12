"""
THIS DB API WILL LET YOU COMMUNICATE WITH ANY TYPE OF DATABASE
"""
import importlib as imp

# API REQUIRED MODULES
from dbexceptions import *

class Database:
    """
        This is major class of this api
    """
    def __init__(self,dbkind,**kwargs):
        """
            dbkind is must argument which can have local or server
        """
        self.conn = None
        self.cur = None
        try:
            self.db_module = imp.import_module(
                kwargs.get('dbmodule')
            )
            self.query_module = imp.import_module(
                kwargs.get('querymodule')
            )
        except Exception as e:
            raise ModuleImportError(str(e))
        else:
            try:
                if dbkind.lower().strip() == "local":
                    self.conn = self.db_module.connect(
                        kwargs.get('dbpath')
                    )
                elif dbkind.lower().strip() == "server":
                    self.conn = self.db_module.connect(
                        host = kwargs.get('host'),
                        port = kwargs.get('port'),
                        user = kwargs.get('user'),
                        password = kwargs.get('password'),
                        database = kwargs.get('database')
                    )
                else:
                    raise ValueError('Invalid dbkind value')
            except Exception as e:
                raise ConnectionOrCursorError(e)
            else:
                self.cur = self.conn.cursor(buffered=True)
    def createtable(self):
        try:
            self.cur.execute(
                self.query_module.create_table
            )
            self.conn.commit()
        except:
            self.conn.rollback()
            raise OperationFailedError('Failed to create the table')
        else:
            return True
    def insertdata(self,data):
        try:
            for f,l,e in data:
                self.cur.execute(
                    self.query_module.insert_data.format(
                        f,l,e
                    )
                )
            self.conn.commit()
        except:
            self.conn.rollback()
            raise OperationFailedError("Insertion Failed")
        else:
            return True
    def readdata(self,nrows=1):
        try:
            self.cur.execute(
                self.query_module.read_data                
            )
        except:
            raise OperationFailedError('Read Failed')
        else:
            return self.cur.fetchmany(nrows)
    def info(self):
        print('DB MODULE : ',self.db_module)
        print('QRY MODULE : ',self.query_module)
        print('IS CONNECTED : ',True if self.conn else False)

    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print('connection destroyed')
                
