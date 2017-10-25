#!/usr/bin/python

import socket,struct,sys

def addressInNetwork(ip,net):
	"Is an address in a network"
	ipaddr = struct.unpack('L',socket.inet_aton(ip))[0]
	netaddr,bits = net.split('/')
	netmask = struct.unpack('L',socket.inet_aton(netaddr))[0] & ((2L<<int(bits)-1) - 1)
	print "ip: " + ip + " ipaddr: " + str(ipaddr) 
	print "nm: " + str(netmask) + " ipaddr & nm " + str(ipaddr & netmask)
	return ipaddr & netmask == netmask

ip = sys.argv[1]
net = "192.168.1.1/24"
print addressInNetwork(ip,net)
