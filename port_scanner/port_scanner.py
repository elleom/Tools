#!/usr/bin/env python

import socket
import argparse
from IPy import IP


def scan(ip_address, port):
    print(ip_address, port)
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f'[*] Port {port} is open')
    except ConnectionError:
        print(f'[*] Port {port} seems to be closed or filtered')

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='target_ip', help="IP to target interface")
    parser.add_argument('--port', dest='port', help="port to scan")
    options = parser.parse_args()
    if not options.target_ip:
        parser.error("[!] Introduce target's IPV4")
    elif not options.port:
        parser.error("[!] Introduce port to scan")
    return options


if '__main__':
    try:
        args = get_arguments()
        scan(args.target_ip, int(args.port))
    except KeyboardInterrupt:
        print('[-] Program terminated')
