import socket
from struct import *

#########################################


def error_checksum(msg):
    #What is error_checksum Algorithm?
    s = 0
    for i in range(0, len(msg), 2) :
        w = msg[i] + (msg[i+1] << 8)
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 6)
    s = ~s & 0xfff
    return s
#########################################


s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

#Payload Data
tcp_payload_data = b"Python 3 Raw Socket!"

#TCP Header
source_port = 4321
dest_port = 22
seq_number = 123
ack_number = 0
offset = 5
reserved = 0
offset = (offset << 4) + reserved
fin = 0
syn = 1
rst = 0
psh = 0
ack = 0
urg = 0
flags = (urg << 5) +(ack << 4) + (psh << 3) + (rst << 2) + (syn << 1) + (fin << 0)
window = socket.htons(5840)
checksum = 0
urgent_pointer = 0

tcp_header = pack("!HHLLBBHHH", source_port,dest_port, seq_number, ack_number, offset, flags, window, checksum, urgent_pointer)

#Pseudo Header
ip_source = "127.0.0.1"
source_ip_address = socket.inet_aton(ip_source)
ip_dest = "127.0.0.1"
dest_ip_address = socket.inet_aton(ip_dest)
placeholder = 0
protocol = socket.IPPROTO_TCP
length = len(tcp_header) + len(tcp_payload_data)

pseudo_header = pack("!4s4sBBH", source_ip_address, dest_ip_address,placeholder,protocol,length)
#한번 사용하고 사라지는 용도

pseudo_header = tcp_payload_data + tcp_header + pseudo_header
tcp_checksum = error_checksum(pseudo_header)
print("TCP Checksum:",(tcp_checksum))

tcp_header = pack("!HHLLBBHHH", source_port, dest_port,seq_number,ack_number,offset, flags, window, tcp_checksum, urgent_pointer)

#IP Header
version = 4
header_length = 5
version_header_length = (version << 4) + header_length
tos = 0
total_length = 0
id = 4321
fragment_offset = 0
ttl = 255
protocol = socket.IPPROTO_TCP
header_checksum = 0
ip_source = "127.0.0.1"
source_ip_address = socket.inet_aton(ip_source)
ip_dest = "127.0.0.1"
dest_ip_address = socket.inet_aton(ip_dest)

ip_header = pack("!BBHHHBBH4s4s",version_header_length,tos,total_length,id,fragment_offset,ttl,protocol,header_checksum,source_ip_address,dest_ip_address)

#IP Packet 에는 Pseudo Header 미포함!!
ip_packet = tcp_payload_data + tcp_header + ip_header

print(s.sendto(ip_packet,(ip_dest,0)))