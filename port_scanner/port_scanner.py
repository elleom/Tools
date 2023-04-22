#!/usr/bin/env python

import socket
import argparse
import header.header_banner
from colorama import Fore, Style
from IPy import IP


def get_ports(ports):
    ports_array = []
    if '/' in ports:
        # handles range
        ports_array = ports.split('/')
        return ports_array, True
    elif '-' in ports:
        ports_array = ports.split('-')
        return ports_array, False
    else:
        ports_array.append(ports)
        return ports_array, False


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


def check_ip(target):
    try:
        IP(target)
        return target
    except ValueError:
        target_ip = socket.gethostbyname(target)
        print(f'[!] {target} resolved to {target_ip}')
        return target_ip


def parse_scan_vars(targets, ports):

    (ports, is_range) = get_ports(ports)

    for target in targets.split(','):
        print(f'[*] Initiating scan on {target}')
        ip_addr = check_ip(target)
        try:
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
    parser.add_argument('--target', dest='target_ip',
                        help="IP/s to target interface - !!! [split different ip using ',']")
    parser.add_argument('--port', dest='port', help="port/s to scan !!! [takes only one linear range. e.g 5/75]")
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
        parse_scan_vars(args.target_ip, args.port)
    except KeyboardInterrupt:
        print('[-] Program terminated')
