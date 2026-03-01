import ipaddress
import subprocess 
from concurrent.futures import ThreadPoolExecutor



def sent_icmp(ip):
    ping = subprocess.run(["ping", "-c", "2", str(ip)], capture_output=True)
    if "100% packet loss" not in ping.stdout.decode():
        print(str(ip))
    return

def main():
    print("WELCOME TO IP SCANNER:")
    ip1 = input("Enter ip1 (format: x.x.x.x):")
    ip2 = input("Enter ip2 (format: x.x.x.x):")


    start_ip = ipaddress.IPv4Address(ip1)
    end_ip   = ipaddress.IPv4Address(ip2)

    with ThreadPoolExecutor(max_workers=50) as executor:
        for ip in range(int(start_ip), int(end_ip) + 1):
            executor.submit(sent_icmp, ipaddress.IPv4Address(ip))

if __name__ == ("__main__"):
    main()
    
