#!/usr/bin/env python

import http
import scapy.all as scapy
import netfilterqueue


def process_packet(packet):
    print(packet)
    print(packet.get_payload())

    scapy_packet = scapy.IP(packet.get_payload())  # wraps the packet into IP layer
    if scapy_packet.hasLayer(scapy.Raw):
        print(scapy_packet.show())  # prints all the packets with useful data (dev only)


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet())
queue.run()