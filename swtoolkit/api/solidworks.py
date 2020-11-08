import os
import subprocess as sb

import win32com.client

from .interfaces.isldworks import ISldWorks
from .modeldoc import ModelDoc


class SolidWorks(ISldWorks):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"<{self.__class__.__name__}><{self.get_process_id()}>"

    def __str__(self):
        return f"{self.__class__.__name__}"

    # def __enter__(self):
    #     pass

    # def __exit__(self, exc_type, exc_value, exc_traceback):
    #     pass

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

    @property
    def process_id(self):
        return self.get_process_id()

    def open(self, path, options=1, configuration=str()):
        """Opens a documents

        :param path: File path
        :type path: str
        :param options: File load options, defaults to 1
        :type options: int, optional
        :param configuration: Specifies configuration to load, defaults to str()
        :type configuration: str, optional
        :raises ValueError: File must be solidworks native
        :return: Error, Warning
        :rtype: int
        """

        if os.path.splitext(path)[1] == ".SLDPRT":
            type_value = 1
        elif os.path.splitext(path)[1] == ".SLDASM":
            type_value = 2
        elif os.path.splitext(path)[1] == ".SLDDRW":
            type_value = 3
        else:
            raise ValueError("Incompatible File Type")

        err, warn = self._opendoc6(path, type_value, options, configuration)
        return err, warn

    def quit(self):
        self.exit_app()

    def get_model(self):
        return ModelDoc()

    def get_documents(self):
        return [ModelDoc(parent) for parent in self._get_documents()]
