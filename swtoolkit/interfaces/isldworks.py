import win32com.client

# import pythoncom


class ISldWorks:
    def __init__(self):
        self.swcom = win32com.client.Dispatch("SldWorks.Application")

    def __enter__(self):
        return self.swcom

    def __exit__(self):
        self.swcom = None
        return True

    @property
    def active_doc(self):
        return self.swcom.ActiveDoc

    @property
    def is_visible(self):
        return self.swcom.Visible

    @property
    def startup_completed(self):
        return self.swcom.StartupProcessCompleted
