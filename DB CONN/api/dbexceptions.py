class ModuleImportError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class ConnectionOrCursorError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OperationFailedError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg