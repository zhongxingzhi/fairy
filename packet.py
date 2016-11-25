def event(func):
    print (func)
    func.event_name = 'event_name'
    return func
#     def wrapper(self):
        # func(self)
        # print("execute")
    # wrapper.evt_name = 'evt_name'
    # return wrapper

class valueType(object):
    pass

class Packet(object):
    def __init__(self):
        self.x = valueType
        self.y = 0
    @property
    def getX(self):
        pass
