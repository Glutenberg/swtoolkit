import subprocess as sb
import win32com.client

from .interfaces.isldworks import ISldWorks, IModelDoc


class SolidWorks(ISldWorks):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_doc = IModelDoc()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    @staticmethod
    def start(*args):
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
    def kill():
        """Force kill SLDWORKS.exe process. """
        sb.call("Taskkill /IM SLDWORKS.exe /F")
