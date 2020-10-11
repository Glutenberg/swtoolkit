import win32com.client


class COM:
    def __init__(self):
        pass

    def connect(self):
        """ Establish connection with Solidworks """

        self.swcom = win32com.client.Dispatch("SldWorks.Application")
        return self.swcom
