import win32com.client

from .interfaces.imodeldocextension import IModelDocExtension


class ModelDocExtension(IModelDocExtension):
    def __init__(self, parent):
        super().__init__(parent)
