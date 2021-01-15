#!/usr/bin/env python

import scapy.all as scapy

######################################################################
# prints summary of fields to set
# scapy.ls(scapy.ARP())
# scapy.ls(scapy.Ether())
'''
    #scapy.ls(scapy.ARP()) OUTPUT EXAMPLE

    hwtype: XShortField = (1)
    ptype: XShortEnumField = (2048)
    hwlen: FieldLenField = (None)
    plen: FieldLenField = (None)
    op: ShortEnumField = (1)
    hwsrc: MultipleTypeField = (None)
    psrc: MultipleTypeField = (None)
    hwdst: MultipleTypeField = (None)
    pdst: MultipleTypeField = (None)
'''
########################################################################


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # alt arp_request.pdst=ip

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    print(arp_request.summary())
    # Ex output ARP who has 192.168.15.133 says 192.168.15.135
    print(broadcast.summary())
    # Ex output 00:0c:29:df:79:3d > ff:ff:ff:ff:ff:ff (0x9000)

    request_broadcast = broadcast / arp_request  # combines both vars
    print(request_broadcast.summary())

    request_broadcast.show()  # prints details
    answered_list = scapy.srp(request_broadcast, timeout=1)[0]  # timeout: waits for a sec (int),
    # otherwise could get stuck

    # print(answered_list.summary())
    # print(unanswered.summary()) not really neaeed :)
    # REMEMBER TO RUN AS SUDO

    for element in answered_list:
        print(element[1].show(), end='\n')


scan("192.168.15.1/24")
