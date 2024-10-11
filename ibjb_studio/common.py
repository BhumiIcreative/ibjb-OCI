def get_field_type(self, field_name):
    """
    Return the field type
    """
    field_info = self.fields_get([field_name], attributes=("type"))
    if field_info:
        return field_info.get(field_name, {}).get("type")
    else:
        return False


def set_customer_field(self, x_field_name, field):
    """
    Function to set the custom field same as studio field if has same field type
    """
    if hasattr(self, x_field_name):
        x_field_type = get_field_type(self, x_field_name)
        custom_field_type = get_field_type(self, field)
        if x_field_type == custom_field_type:
            print('\n\n\n\nx_field_type == custom_field_type')
            setattr(self, field, getattr(self, x_field_name, False))
