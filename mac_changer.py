import subprocess

iface = "wlan0"
ether = "00:11:22:33:44:55"

print('[*] Changing MAC Address for' + iface)
print('[*] MAC Addrress set to' + ether)

subprocess.call(["ifconfig", iface, "down"], shell=True) # input hygiene
subprocess.call(["ifconfig", iface, "hw", ether],  shell=True)
subprocess.call(["ifconfig", iface, "up"], shell=True)