from .blueprint import *


@packet
class GamePacket(object):

    @field(1, uint)
    def packet_len(self): pass

    @field(2, uint)
    def packet_sum(self): pass


@packet
class ConnectPacket(GamePacket):

    @field(1, int)
    def connect_cmd(self): pass


@event(8)
class PunchPacket(ConnectPacket):

    @field(1, int)
    def process_id(self): pass

    @field(2, int)
    def machine_id(self): pass
