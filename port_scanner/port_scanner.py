#!/usr/bin/env python

import socket
import argparse
import header.header_banner
from colorama import Fore, Style


def get_ports(ports):
    if '/' in ports:
        # handles range
        return ports.split('/'), True
    elif '-' in ports:
        return ports.split('-'), False
    else:
        return ports, False


def get_port_status(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f' ... port ' + Fore.GREEN + 'OPEN' + Style.RESET_ALL)
        sock.close()
    except ConnectionError:
        print(f' ... port {port} seems to be '
              + Fore.RED + 'CLOSED'
              + 'or' + Fore.WHITE
              + 'FILTERED'
              + Style.RESET_ALL)


def parse_scan_vars(ip_address, ports, url=None):

    (ports, is_range) = get_ports(ports)

    try:
        if url:
            ip_address = socket.gethostbyname(url)
            print(f'[!] {url} resolved to {ip_address}')
        sock = socket.socket()

        if is_range:
            print(f'[*] Scanning range {ports[0]}:{ports[1]}')
            for port in range(int(ports[0]), int(ports[1])):
                get_port_status(ip_address, port)
        else:
            for port in ports:
                print(f'[*] Scanning port {port}', end='')
                get_port_status(ip_address, int(port))

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
        parse_scan_vars(args.target_ip, args.port, args.url)
    except KeyboardInterrupt:
        print('[-] Program terminated')
