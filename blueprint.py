import struct

class FieldObject(object):

    def __init__(self, value_type):
        self.value = value_type()

    def __get__(self, obj, cls):
        return self.value

    def __set__(self, obj, val):
        self.value = val


def packet(packet_id):
    def _wraper(cls):
        cls.__packet_id__ = packet_id
        return cls

    return _wraper

def event(event_id):
    def _wraper(cls):
        cls.__event_id__ = event_id
        cls.__meta_fields__ = {}
        for attr in cls.__dict__:
            if hasattr(attr, "__field_id__"):
                setattr(cls, attr, FieldObject(attr.__field_type__))
                cls.__meta_fields__[attr] = (attr.__field_id__, attr.__field_type__)

        return cls

    return _wraper


def field(field_id, field_type):
    def _wraper(func):
        func.__field_id__ = field_id
        func.__field_type__ = data_type
        return func

    return _wraper


class short_type(object):
    __FORMAT__ = "=h"
    def __init__(self):
        self.data = 0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class ushort_type(object):
    __FORMAT__ = "=H"
    def __init__(self):
        self.data = 0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class int_type(object):
    __FORMAT__ = "=i"
    def __init__(self):
        self.data = 0
    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class uint_type(object):
    __FORMAT__ = "=I"
    def __init__(self):
        self.data = 0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class int64_type(object):
    __FORMAT__ = "q"
    def __init__(self):
        self.data = 0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class uint64_type(object):
    __FORMAT__ = "Q"
    def __init__(self):
        self.data = 0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class float_type(object):
    __FORMAT__ = "=f"
    def __init__(self):
        self.data = 0.0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class double_type(object):
    __FORMAT__ = "d"
    def __init__(self):
        self.data = 0.0

    def serialize(self, out_stream):
        out_stream.write(struct.pack(self.__FORMAT__, self.data))


class string_type(object):
    def __init__(self):
        self.data = ""

    def serialize(self, out_stream):
        out_stream.write(struct.pack("=i", len(self.data)))
        out_stream.write(struct.pack("={0}s".format(len(self.data)), self.data))
        out_stream.write(b'\0')


class bytes_type(object):
    def __init__(self):
        self.data = bytes()

    def serialize(self, out_stream):
        out_stream.write(struct.pack("=i", len(self.data)))
        out_stream.write(struct.pack("={0}s".format(len(self.data)), self.data))


class list_type(object):
    def __init__(self):
        self.data = None

    def serialize(self, out_stream):
        out_stream.write(struct.pack("=i", len(self.data)))
        for d in self.data:
            d.serialize(out_stream)


class user_type(object):

    @field(1, type(string_type))
    def user_name(self): return "anti"

    @field(2, type(int_type))
    def user_age(self): return 18


@packet(100)
class AccountPacket(object):

    @field(1, type(1))
    def connect_cmd(self): return 1

    @field(2, type(1))
    def hash_value(self): return 0

@event(1000)
class Event(object):

    @field(1, type(1))
    def event_id(self): return 0

    @field(2, type(""))
    def event_name(self): return "hello!"

    def event_hash(self): return 100

    def event_size(self): return 100
