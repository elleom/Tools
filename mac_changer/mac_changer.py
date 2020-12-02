#!/usr/bin/env python

import subprocess
import optparse
import re


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
# end get_arguments() #


def change_mac(iface, new_mac):

    print('[*] Changing MAC Address for ' + iface)
    print('[*] MAC Address set to ' + new_mac)

    subprocess.call(["ifconfig", iface, "down"])  # input hygiene
    subprocess.call(["ifconfig", iface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", iface, "up"])
# end change_mac() #


def get_mac_address(iface):
    ifconfig_results = subprocess.check_output(['ifconfig', iface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_results))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address")


options = get_arguments()  # read first

current_mac = get_mac_address(options.interface)
print('[*] Current MAC =' + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_mac_address(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC changed")
else:
    print("[-] MAC address did not changed")

