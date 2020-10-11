import win32com.client
import pythoncom


class IModelDoc:
    def __init__(self, swcom):
        self.swcom = swcom
