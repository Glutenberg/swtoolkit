from .interfaces.icustompropertymanager import ICustomPropertyManager
from .enums.enum_types import CustomInfoType
from .enums.enum_options import CustomPropertyAddOption
from .enums.enum_results import (
    CustomInfoAddResult,
    CustomInfoDeleteResult,
    CustomInfoGetResult,
    CustomInfoSetResult,
)


class CustomPropertyManager(ICustomPropertyManager):
    def __init__(self, parent, config_name):
        super().__init__(parent, config_name)

    def get_all(self):
        """Gets all the custom properties for the current active configuration

        Returns:
            List of Tuples: A list of tuples; each containing the following:
                1. Property Name,
                2. Property Type,
                3. Property Value,
                4. Resolved - A result code,
                5. Property Link

        """
        arg1, arg2, arg3, arg4, arg5 = self.get_all3()
        return list(
            zip(
                arg5.value,
                CustomInfoType(arg4.value),
                arg3.value,
                CustomInfoGetResult(arg2.value),
                arg1.value,
            )
        )

    def add(self, field_name, field_type, field_value, overwrite_existing):

        _field_type = CustomInfoType[field_type.upper().replace(" ", "_")].value
        _overwrite_existing = CustomPropertyAddOption[
            overwrite_existing.upper().replace(" ", "_")
        ].value

        retval = self._add3(
            field_name, _field_type, field_value, _overwrite_existing
        )

        return CustomInfoAddResult(retval)

    def delete(self, field_name):

        retval = self._delete2(field_name)
        return CustomInfoDeleteResult(retval)

    def get(
        self,
        field_name,
        use_cached,
        val_out,
        resolved_val_out,
        was_resolved,
        link_to_property,
    ):
        pass

    def set_(self, field_name, field_value):
        retval = self._set2(field_name, field_value)
        return CustomInfoSetResult(retval)
