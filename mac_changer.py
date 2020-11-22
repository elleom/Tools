#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--iface", dest="interface", help="Interface to change MAC")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC")

(options, arguments) = parser.parse_args()

iface = options.interface
new_mac = options.new_mac

print('[*] Changing MAC Address for' + iface)
print('[*] MAC Addrress set to' + new_mac)

subprocess.call(["ifconfig", iface, "down"]) # input hygiene
subprocess.call(["ifconfig", iface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", iface, "up"])