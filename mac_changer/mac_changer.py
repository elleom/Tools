#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--iface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:  # if not null
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify the new MAC, use --help for more info.")
    return options


def change_mac(iface, new_mac):

    print('[*] Changing MAC Address for' + iface)
    print('[*] MAC Addrress set to' + new_mac)

    subprocess.call(["ifconfig", iface, "down"])  # input hygiene
    subprocess.call(["ifconfig", iface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", iface, "up"])


options = get_arguments()  # read first
change_mac(options.interface, options.new_mac)

