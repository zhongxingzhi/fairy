import io
import struct

type_map = {}
type_map["int"] = ("=i", lambda x : x)
type_map["uint"] = ("=I", lambda x : x.value)
type_map["int64"] = ("=q", lambda x : x.value)
type_map["uint64"] = ("=Q", lambda x : x.value)

def is_event(obj):
    return hasattr(obj, "__event_id__")

def is_packet(obj):
    return hasattr(obj, "__packet_id__")

def get_bytes(val):
    tm = type_map[type(val).__name__]
    return struct.pack(tm[0], tm[1](val))

class Serializer(object):

    def serialize(self, obj):
        if not is_event(obj):
            return None

        out_stream = io.BytesIO()
        fields = sorted(obj.__meta_fields__.items(), key = lambda x: x[1][0])
        for (fkey, fval) in fields:
            out_stream.write(get_bytes(getattr(obj, fkey)))

        return out_stream.getvalue()
