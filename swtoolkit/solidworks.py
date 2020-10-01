import subprocess as sb
import win32com.client

# import pythoncom

from .interface.isldworks import ISldWorks


class SolidWorks(ISldWorks):
    def __init__(self):
        pass

    @staticmethod
    def start(self, *args):
        """Starts instance of SolidWorks.
        :param: The last 2 digits of your solidworks distribution release year.
        """

        if not args:
            SW_PROCESS_NAME = (
                r"C:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/SLDWORKS.exe"
            )
            sb.Popen(SW_PROCESS_NAME)
        else:
            year = int(args[0][-1])
            SW_PROCESS_NAME = f"SldWorks.Application.{(20 + (year - 2))}"
            win32com.client.Dispatch(SW_PROCESS_NAME)

    @staticmethod
    def kill(self):
        """Force kill SLDWORKS.exe process. """
        sb.call("Taskkill /IM SLDWORKS.exe /F")

    @staticmethod
    def connect(self):
        """ Establish connection with Solidworks """

        self.swcom = win32com.client.Dispatch("SldWorks.Application")
        return self.swcom
