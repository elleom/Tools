#!/usr/bin/env python

# sudo iptables -I FORWARD --jump NFQUEUE --queue-num 0
# requires netfilterqueue , not available for python 3.7+

import netfilterqueue


def process_packet(packet):
    print(packet)


queue = netfilterqueue.Netfilterqueue
queue.bind(0, process_packet)
queue.run()