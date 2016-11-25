import io


class Serializer(object):

    def serialize(self, obj):
        out_stream = io.BytesIO()
        props = (getattr(obj, p) for p in dir(obj) if hasattr(getattr(obj, p), "__field_id__"))

        #sort

        for p in props:
            p.serialize(out_stream)

        return out_stream.getvalue()
