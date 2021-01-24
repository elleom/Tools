#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet, filter="tcp")  # prn= callback
    # available filters
    # bps syntax https://biot.com/capstats/bpf.html
    # port 21
    # udp
    # tpc


def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load) 


sniff("eth0")
