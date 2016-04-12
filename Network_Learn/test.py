
#!/usr/bin/env python
# Python Network Programming Cookbook - Chapter - 1
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.
import socket
from binascii import hexlify
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print "IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)


def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 3306, 8080, 110, 27]:
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, 'tcp'))
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, 'udp'))


def convert_integer():
    data = 1234
    # 32-bit
    print "Original: %s => Long host byte order: %s, Network byte order: %s"\
        %(data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print "Original: %s => Short host byte order: %s, Network byte order: %s"\
        %(data, socket.ntohs(data), socket.htons(data))


def test_socket_timeout():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Default socket timeout: %s" %s.gettimeout()
        s.settimeout(10)
        print "Current socket timeout: %s" %s.gettimeout()


if __name__ == '__main__':
    # convert_ip4_address()

    # find_service_name()

    # convert_integer()

    test_socket_timeout()
