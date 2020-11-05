class ICustomPropertyManager:
    def __init__(self, parent, config_name=str()):
        self._instance = parent.CustomPropertyManager(config_name)

    @property
    def count(self):
        return self._instance.Count

    @property
    def link_all(self):
        return

    @property
    def owner(self):
        return self._instance.Owner

    def add3(self):
        pass

    def delete2(self):
        pass

    def get6(self):
        pass

    def set2(self):
        pass

    def get_all3(self):
        pass

    def get_type2(self):
        pass

    def is_custom_property_editable(self):
        pass

    def link_property(self):
        pass
