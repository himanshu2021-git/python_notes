""" 
    this module contains the exception of api
"""

class CouldNotReadFileError(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

class ImproperCallError(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg