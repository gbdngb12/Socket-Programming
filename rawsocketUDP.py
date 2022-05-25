import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

source_port = 4321
dest_port = 22

length = 0
checksum = 0

udp_header = struct.pack("!4H",source_port, dest_port, length, checksum)

print(udp_header)