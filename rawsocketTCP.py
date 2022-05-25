import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

source_port = 4321
dest_port = 22

seq_number = 123

ack_num = 0

offset = 5
reserved = 0
offset = (offset << 4) + reserved

fin = 0
syn = 1
rst = 0
psh = 0
ack = 0
urg = 0

flags = (urg << 5) + (ack << 4) + (psh << 3) + (rst << 2)+(syn << 1) + (fin << 0)

window = socket.htons(5840)

checksum = 0
urgent_pointer = 0

tcp_header = struct.pack("!HHLLBBHHH",source_port, dest_port, seq_number, ack_num,offset,flags,window,checksum, urgent_pointer)

ip_source = "127.0.0.1"
source_ip_address = socket.inet_aton(ip_source)

ip_dest = "127.0.0.1"
dest_ip_address = socket.inet_aton(ip_dest)

placeholder = 0
protocol = socket.IPPROTO_TCP

tcp_length = len(tcp_header)

pseudo_header = struct.pack("!4s4sBBH", source_ip_address, dest_ip_address, placeholder, protocol, tcp_length)
print(pseudo_header)
pseudo_header = pseudo_header + tcp_header

#tcp_checksum = checksum(pseudo_header)

