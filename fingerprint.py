import socket
import nmap,os,sys 
import portscanner


def get_service_banner(ip,port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip,int(port)))
        sock.send(b"GET /HTTP/1.1\r\n Host: "+ip.encode()+b"\r\n\r\n")
        banner=sock.recv(1024)
        socket.close()

        return banner.decode("utf-8",errors='ignore')
    except Exception:
        return None

def scan_host(ip,ports):
    nm=nmap.PortScanner() 
    nm.scan(ip,ports)
    host_infos=[]
    for proto in nm[ip].all_protocols():
        lport=nm[ip][proto].keys()
        for port in lport:
            host_info={
                'ip':ip,
                'os':nm[ip].get('osclass',{}).get('osfamily','Unknown'),
                'port':port,
                'name':nm[ip][proto][port]['name'],
                'product':nm[ip][proto][port]['product'],
                'version':nm[ip][proto][port]['version']
            }
            host_infos.append(host_info)
    return host_infos

def service_fp():
    ip = input("Enter the IP address :")
    ports=input("Enter the port (Multiple port should be space separated): ")
    port_list=ports.split()
    print(f"Scanning IP : {ip}")
    for port in port_list:
        print(f"Scanning port{port} on IP {ip}")
        banner= get_service_banner(ip,port)
        if banner:
            print(f"Service banner for port {port} on IP {ip} : \n {banner}\n")
        else:
            print(f"No Service banner found for port {port} on IP {ip}")
    #print(port_list)

def os_fp():
    ip = input("Enter the IP address :")
    ports=input("Enter the port (Multiple port should be space separated): ")
    port_list=ports.split()
    print(f"Scanning IP : {ip}")
    print(f"Scanning PORT : {port_list}")

    # sys.stdout.write("Scanning")
    sys.stdout.flush()
    print("\nScan Results\n")
    for port in port_list:
       # print(f"Scanning port{port} on IP {ip}")
        host_infos=scan_host(ip,port)
        for host_info in host_infos:
              print(f"IP: {host_info['ip']}")
              print(f"OS: {host_info['os']}")
              print(f"Port: {host_info['port']}")
              print(f"Name: {host_info['name']}")
              print(f"Product: {host_info['product']}")
              print(f"Version: {host_info['version']}")
              print("-"*30)

def main1():
     resp = input("""
Enter the Scan option for the IP.
1. Network IP & Port Scanner
2. Service Fingerprinting
3. OS Fingerprinting \n""")
     if resp=='1':
         portscanner.portScanner()
     elif resp=='2':
         os_fp()
     elif resp=='3':
         service_fp()
#service_fp()
#os_fp()


