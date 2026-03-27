import re

def check_ip(ip):
    # IPv4: 4 groups of 0-255 separated by dots
    ipv4 = r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
    # IPv6: 8 groups of 1-4 hex characters separated by colons
    ipv6 = r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$'
    
    if re.match(ipv4, ip): return 'IPv4'
    if re.match(ipv6, ip): return 'IPv6'
    return 'Neither'
