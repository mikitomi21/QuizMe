from django.db import models


class TypeField(models.CharField):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"

    OPTIONS = [
        (CLOSED, "close"),
        (OPEN, "open"),
        (MULTIPLE_CHOICE, "multiple_choice"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = self.OPTIONS
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value

    def to_python(self, value):
        if isinstance(value, str) or value is None:
            return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
