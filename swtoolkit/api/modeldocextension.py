import win32com.client

from .interfaces.imodeldocextension import IModelDocExtension


class ModelDocExtension(IModelDocExtension):
    def __init__(self):
        super().__init__()
