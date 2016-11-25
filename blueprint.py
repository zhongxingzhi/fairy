import struct


class FieldObject(object):

    def __init__(self, value_type):
        self.value = value_type()

    def __get__(self, obj, cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val


def event(event_id):
    def _wraper(cls):
        cls.__event_id__ = event_id
        cls.__meta_fields__ = {}

        for attr in cls.__dict__:
            fi = getattr(cls, attr)
            if hasattr(fi, "__field_id__"):
                cls.__meta_fields__[attr] = (fi.__field_id__, fi.__field_type__)
                setattr(cls, attr, FieldObject(fi.__field_type__))

        return cls

    return _wraper


def field(field_id, field_type):
    def _wraper(func):
        func.__field_id__ = field_id
        func.__field_type__ = field_type
        return func

    return _wraper


class Student(object):
    def __init__(self):
        self.name = "tom"
        self.id = 11


@event(1000)
class Event(object):

    @field(1, int)
    def event_id(self): pass

    @field(2, float)
    def event_rate(self): pass

    @field(3, Student)
    def student_name(self): pass
