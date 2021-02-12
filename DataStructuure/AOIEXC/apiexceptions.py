class ReadFailedError(Exception):
	def __init__(self,msg,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.msg = msg
	
	def __str__(self):
		return self.msg

class WriteFailedError(Exception):
	def __init__(self,msg,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.msg = msg
	
	def __str__(self):
		return self.msg

