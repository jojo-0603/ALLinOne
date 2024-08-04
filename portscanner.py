from scapy.all import ICMP,IP,TCP,sr1,sr
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor,as_completed
from threading import Lock
import os

print_lock =Lock()
def ping(host):
  try:
    response =sr1(IP(dst=str(host))/ICMP(),timeout=1,verbose=0)
    if response is not None:
        return str(host)
  except (Warning,Exception):
      pass
  return None

def ping_sweep(network,netmask):
    live_hosts=[]
    num_threads =os.cpu_count()
    hosts = list(ip_network(network + '/' +netmask).hosts())
    tot_hosts = len(hosts)
    try:  
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = {executor.submit(ping,host):host for host in hosts}
                for i,future in enumerate(as_completed(futures),start=1):
                    host =futures[future]
                    result = future.result()
                    with print_lock:
                        print(f"Scanning {i}/{tot_hosts}",end="\r")
                        if result is not None:
                            print(f"\nHost {host} is online")
                            live_hosts.append(result)
    except (Warning,Exception):
     pass
    return live_hosts
    

def scan_port(ip,port):
 try:
     response =sr1(IP(dst=ip)/TCP(dport=port,flags="S"),timeout=1,verbose=0)
     if response is not None and response[TCP].flags =='SA':
        return port
 except (Warning,Exception):
     pass
     return None

def port_scan(ip,ports):
    open_ports=[]
    num_threads=os.cpu_count()
    total_ports=len(ports)
    try:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = {executor.submit(scan_port,ip,port):port for port in ports}
            for i,future in enumerate(as_completed(futures),start=1):
                port =futures[future]
                result = future.result()
                with print_lock:
                    print(f"Scanning {i}/{total_ports}",end="\r")
                    if result is not None:
                        print(f"\nPort {port} is open on host {ip}")
                        open_ports.append(result)
    except (Warning,Exception):
        pass
    return open_ports

def get_live_hosts_and_ports(network,netmask='24'):
    live_hosts=ping_sweep(network,netmask)
    ports=range(1,1024)
    host_port_mapping={}
    for host in live_hosts:
        open_ports = port_scan(host,ports)
        host_port_mapping[host]=open_ports

    return host_port_mapping

def portScanner():
    network=input("Enter the starting ip address of the network to scan(eg:xxx.xxx.xxx.0): ")
    netmask=input("Enter the subnet mask : ")
    host_port_mapping=get_live_hosts_and_ports(network,netmask)
    for host,open_ports in host_port_mapping.items():
        print(f"\nHost {host} has the following open ports : {open_ports}")


#portScanner()