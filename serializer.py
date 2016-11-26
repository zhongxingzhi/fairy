import io
import struct


def is_event(obj):
    return hasattr(obj, "__event_id__")

def get_bytes(t, val):
    return struct.pack("=i", val)

class Serializer(object):

    def serialize(self, obj):
        if not is_event(obj):
            return None

        out_stream = io.BytesIO()
        fields = sorted(obj.__meta_fields__.items(), key = lambda x: x[1][0])
        for (fkey, fval) in fields:
            out_stream.write(get_bytes(fval.__field_type__, getattr(obj, fkey)))

        return out_stream.getvalue()
