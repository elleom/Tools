#!/usr/bin/env python

import socket
import argparse
import header.header_banner


def scan(ip_address, port, url=None):
    try:
        if url:
            ip_address = socket.gethostbyname(url)
            print(f'[!] {url} resolved to {ip_address}')
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f'[*] Port {port} is open')
    except ConnectionError:
        print(f'[*] Port {port} seems to be closed or filtered')


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='target_ip', help="IP to target interface")
    parser.add_argument('--port', dest='port', help="port to scan")
    parser.add_argument('--url', dest='url', help="Target's URL")
    options = parser.parse_args()
    if not options.target_ip and not options.url:
        parser.error("[!] Introduce target's IPV4 or URL")
    elif not options.port:
        parser.error("[!] Introduce port to scan")
    return options


if '__main__':
    try:
        header.header_banner.print_header()
    except ModuleNotFoundError:
        print('[!] MuiausOnTheWire :) is launching...')
    try:
        args = get_arguments()
        scan(args.target_ip, int(args.port), args.url)
    except KeyboardInterrupt:
        print('[-] Program terminated')
