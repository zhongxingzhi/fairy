import struct


MAX_CLASS_FIELD_NUM = 1000

def echo_attributes(obj):
    print("attributes for {0}".format(obj.__name__))
    for a in dir(obj):
        print("{0}: {1}".format(a, getattr(obj, a)))


class FieldObject(object):

    def __init__(self, value_type):
        self.value = value_type()

    def __get__(self, obj, cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val

def packet(cls):
    if len(cls.__base__) == 1 and hasattr(cls.__base__[0], "__packet_id__"):
        cls.__packet_id__ = cls.__base__[0].__packet_id__ + MAX_CLASS_FIELD_NUM
    else:
        cls.__packet_id__ = 0

    return cls

def event(event_id):
    def _wraper(cls):
        cls = packet(cls)
        cls.__event_id__ = event_id
        cls.__meta_fields__ = {}

        for attr in dir(cls):
            fi = getattr(cls, attr)
            if hasattr(fi, "__field_id__"):
                echo_attributes(fi)
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


class uint(object):

    def __init__(self):
        self.value = 0

    def __get__(self, obj, cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val


class int64(object):

    def __init__(self):
        self.value = 0

    def __get__(self, obj ,cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val


class uint64(object):

    def __init__(self):
        self.value = 0

    def __get__(self, obj, cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val
