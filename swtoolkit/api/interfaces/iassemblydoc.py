import win32com.client
import pythoncom


class IAssemblyDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    def _get_components(self, top_level_only: bool):
        """Gets all of the components in the active configuration of this
        assembly.

        Args:
            top_level_only (bool): True to get only the top-level components of
            the FeatureManager design tree, false to get both the top-level and
            child components in the FeatureManager design tree

        Returns:
            COM Object: [description]
        """
        arg = win32com.client.VARIANT(pythoncom.VT_BOOL, top_level_only)
        return self._instance.GetComponents(arg)

    def _get_component_by_id(self, component_id: int):
        """Gets a top-level assembly component using its component ID.

        Args:
            component_id (int): Component ID of top-level assembly component

        Returns:
            System_object: Top-level component
        """
        arg = win32com.client.VARIANT(pythoncom.VT_I4, component_id)
        return self._instance.GetComponentsByID(arg)
