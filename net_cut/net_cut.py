#!/usr/bin/env python

# sudo iptables -I FORWARD --jump NFQUEUE --queue-num 0
# requires netfilterqueue , not available for python 3.7+ via pip,
# install from source
# https://github.com/kti/python-netfilterqueue

# git clone git@github.com:kti/python-netfilterqueue.git
# cd python-netfilterqueue
# python setup.py install


import netfilterqueue


def process_packet(packet):
    print(packet)


queue = netfilterqueue.Netfilterqueue
queue.bind(0, process_packet)
queue.run()