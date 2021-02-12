class RaisedFailedError(Exception):
    def __init__(self,msg,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.msg=msg
    def __str__(self):
        self.msg=msg


