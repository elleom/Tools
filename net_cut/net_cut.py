#!/usr/bin/env python

# sudo iptables -I FORWARD --jump NFQUEUE --queue-num 0 //to try on a diff device

# sudo iptables -I INPUT --jump NFQUEUE --queue-num 0 //to try on local device
# sudo iptables -I OUTPUT --jump NFQUEUE --queue-num 0

# requires netfilterqueue , not available for python 3.7+ via pip,
# install from source
# https://github.com/kti/python-netfilterqueue

# git clone git@github.com:kti/python-netfilterqueue.git
# cd python-netfilterqueue
# python setup.py install

import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    print(packet)
    print(packet.get_payload())  # needs to be converted to a scapy packet

    scapy_packet = scapy.IP(packet.get_payload())  # wraps the packet into IP layer
    if scapy_packet.haslayer(scapy.DNSRR):
        print(scapy_packet.show())

    # packet.drop()  # choose what to do and uncomment
    packet.accept()  # choose what to do and uncomment


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)  # 0 STANDS FOR THE QUEUE NUMBER
queue.run()