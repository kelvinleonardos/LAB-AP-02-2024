import re

def check_ip_address(ip):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    
    return "Bukan IP Address"


N = int(input("Masukkan jumlah baris: "))
for a in range(N):
    ip = input()
    print(check_ip_address(ip))
