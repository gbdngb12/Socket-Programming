import socket
from struct import *

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

Type = 8
code = 0
checksum = 0

id = 0x0001
seq = 13

icmp_header = pack("!BBHHH", Type, code,checksum, id, seq)

print(icmp_header)