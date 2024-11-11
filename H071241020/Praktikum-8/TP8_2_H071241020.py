import re

def is_ipv4(ip):
    ipv4_pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        for part in parts:
            if not (0 <= int(part) <= 255):
                return False
        return True
    return False

def is_ipv6(ip):
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return re.match(ipv6_pattern, ip) is not None

def check_ip_address(n, ip_list):
    for ip in ip_list:
        if is_ipv4(ip):
            print("IPv4")
        elif is_ipv6(ip):
            print("IPv6")
        else:
            print("Bukan IP Address")

n = int(input("Masukkan jumlah baris: "))

ip_list = []
for _ in range(n):
    ip_list.append(input())

check_ip_address(n, ip_list)

#CONTOH INPUTAN UNTUK MENDETEKSI IPV4 : 121.203.197.20
#CONTOH INPUTAN UNTUK MENDETEKSI IPV6 : 2001:0db8:0000:0000:0000:ff00:0042:8329