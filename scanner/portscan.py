import socket
import optparse
from concurrent.futures import ThreadPoolExecutor


parser = optparse.OptionParser()
parser.add_option('-i', '--ip', action="store", dest="ip", help="specify ip target")

options, args = parser.parse_args()
if not options.ip:
    print ("[+] Specify an ip target")
    print ("[+] Example usage (no cracking password): portscan.py -i 192.168.1.1")
    exit()
ip = options.ip

def client_program(host, port):
    try:
        # create client socket instance
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

        # connect socket to server
        client_socket.connect((host, port))
        print(f"Open port: {port}")
    except:
        pass

def main():
     with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(1, 65535):
            executor.submit(client_program, ip, port)  # Pass both ip and port to the function

print("end")
    

if __name__ == '__main__':
    main()
