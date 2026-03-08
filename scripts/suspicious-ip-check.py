import ipaddress

suspicious_ips = ["192.168.1.200", "10.0.0.150"]

for ip in suspicious_ips:
    address = ipaddress.ip_address(ip)
    print(f"Checking IP: {address}")
