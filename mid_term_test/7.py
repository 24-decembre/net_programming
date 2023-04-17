import struct
import binascii
class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(unpacked_udphdr):
    return unpacked_udphdr[0]

def getDstPort(unpacked_udphdr):
    return unpacked_udphdr[1]

def getLength(unpacked_udphdr):
    return unpacked_udphdr[2]

def getChecksum(unpacked_udphdr):
    return unpacked_udphdr[3]


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))
print(struct.unpack('!HHHH', packed_udphdr))
print("Source Port:", getSrcPort(unpack_Udphdr(packed_udphdr)))
print("Destination Port:", getDstPort(unpack_Udphdr(packed_udphdr)))
print("Length:", getLength(unpack_Udphdr(packed_udphdr)))
print("Checksum:", getChecksum(unpack_Udphdr(packed_udphdr)))
