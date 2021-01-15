#!/usr/bin/env python

import scapy.all as scapy
import argparse

######################################################################
# prints summary of fields to set
# scapy.ls(scapy.ARP())
# scapy.ls(scapy.Ether())
from pip._internal.cli.cmdoptions import verbose

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

    # print(arp_request.summary())
    # Ex output ARP who has 192.168.15.133 says 192.168.15.135
    # print(broadcast.summary())
    # Ex output 00:0c:29:df:79:3d > ff:ff:ff:ff:ff:ff (0x9000)

    request_broadcast = broadcast / arp_request  # combines both vars
    # print(request_broadcast.summary())

    # request_broadcast.show()  # prints details
    answered_list = scapy.srp(request_broadcast, timeout=1, verbose=False)[0]  # timeout: waits for a sec (int),
    # otherwise could get stuck

    # print(answered_list.summary())
    # print(unanswered.summary()) not really needed :)
    # REMEMBER TO RUN AS SUDO

    clients_list = []
    for element in answered_list:
        # print(element[1].show(), end='\n')
        # print(element[1].psrc, element[1].hwdst, sep="\t\t" )
        client_dic = {"ip": element[1].psrc, "mac": element[1].hwdst}
        clients_list.append(client_dic)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS --------------")
    for client in results_list:
        print(client)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", dest="ip_range", help="INTRODUCE IP RANGE / 16 /24")
    options = parser.parse_args()
    if not options:  # if not null
        parser.error("[-] Please specify an ip range, EX: '10.0.0.1/24' - use --help for more info.")
    return options


args_range = get_arguments()
scan_results = scan(args_range.ip_range)  # change ip range here
print_result(scan_results)



