"""
THIS DB API WILL LET YOU COMMUNICATE WITH ANY TYPE OF DATABASE

"""
import importlib as imp
from dbexceptions import *
class Database:
    """
    THIS IS MAJOR CLASS OF THIS API
    """
    def __init__(self,dbkind,**kwargs): #in dbkind we tell on which kind of db we want to communicate like local or sever db
        """
        dbkind is must argument which can have local or server
        """
        if dbkind.lower().strip() =="local":
            try:
                self.dbmodule=imp.import_module(
                kwargs.get('dbmodule')
            )
            self.querymodule = imp.import_module(
                kwargs.get('querymodule')
            )
            except Exception as e:
                raise ModuleImportError(str(e))
        else:
            try:
                if dbkind.lower().strip()=="local":
                    self.conn=self.db_module.connect(
                        kwargs.get('dbpath')
                    )
                elif dbkind.lower().strip()="server":
                    self.conn=self.db_module.connect(
                        host=kwargs.get('host'),
                        port=kwargs.get('port'),
                        username=kwargs.get('username'),
                        hpasswordkwargs.get('password'),
                        database=kwargs.get('database'),
                    )
                else:
                    raise ValueError('Invalid Value')
            except Exception as e:
                raise ConnectionOrCursorError(r)
            else:
                self.cur=self.conn.cursor()      
    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print('Connection destroyed') 