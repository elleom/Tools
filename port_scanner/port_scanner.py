#!/usr/bin/env python

import socket
import argparse
import header.header_banner
from colorama import Fore, Style

banners_list = []  # stores banners to display at the end of each target scan


def get_ports(ports):
    if '/' in ports:
        # handles range
        return ports.split('/'), True
    elif '-' in ports:
        return ports.split('-'), False
    else:
        return ports, False


def get_banner(sock):
    return sock.recv(1024)


def get_port_status(ip_address, port):

    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_address, port))
        print(f' ... port {port} is ' + Fore.GREEN + 'OPEN' + Style.RESET_ALL)
        try:
            banner = get_banner(sock)
            print(f'[+] Open port {str(port)}: \n {str(banner)}')
        except:
            print(f'[+] Open port {str(port)} \'s banner is hidden')
        sock.close()
    except TimeoutError or ConnectionError:
        print(f' ... port {port} seems to be'
              , Fore.RED + 'CLOSED'
              , Fore.LIGHTWHITE_EX + 'or'
              , Fore.YELLOW + 'FILTERED'
              + Style.RESET_ALL, sep=' ')


def parse_scan_vars(targets, ports, url=None):

    (ports, is_range) = get_ports(ports)

    for ip_addr in targets.split(','):
        print(f'[*] Initiating scan on {ip_addr}')
        try:
            if url:
                targets = socket.gethostbyname(url)
                print(f'[!] {url} resolved to {targets}')
            if is_range:
                print(f'[*] Scanning range {ports[0]}:{ports[1]}')
                for port in range(int(ports[0]), int(ports[1])+1):
                    get_port_status(ip_addr, port)
            else:
                for port in ports:
                    print(f'[*] Scanning port {port}', end='')
                    get_port_status(ip_addr, int(port))
        except ConnectionError:
            if port == [ports[-1]]:
                continue
            else:
                print(f'[*] Port {port} seems to be closed or filtered')

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='target_ip', help="IP/s to target interface - !!! [split differnent ip using ',']")
    parser.add_argument('--port', dest='port', help="port/s to scan !!! [takes only one linear range. e.g 5/75]")
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
