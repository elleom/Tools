#!/usr/bin/env python

import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet, filter="tcp")  # prn= callback
    # available filters
    # bps syntax https://biot.com/capstats/bpf.html
    # port 21
    # udp
    # tpc


def process_sniff_packet(packet):
    print(packet)


sniff("eth0")
