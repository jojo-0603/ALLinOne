import nmap 
import scapy.all as scapy
import subdomain as sd
import password as passwd
scan = nmap.PortScanner()
import fingerprint
import pprint
#subdomain ='accounts'



    #    print("Subdomain not found")
    #    quit()

def scanner (ip):
   # scapy.arping(ip)
   request= scapy.ARP(pdst=ip)# ARP request
   broadcast= scapy.Ether()
   broadcast.dst="ff:ff:ff:ff:ff:ff" #broadcast MAC address
   req_broad = broadcast/request
   res1,res2= scapy.srp(req_broad,timeout=1)
   #scapy.ls(scapy.Ether())
   for i in res1:
      print(i[1])



if __name__ == "__main__":
  while True: 
    print ("\t\t\tHELLO ALLinONE USER ")
    print("<----------------------------ALLinONE------------------------------------>")
    ip_addr = '192.168.29.211'
    #input("Enter IP address : ")
    print (f"The Ip entered is :{ip_addr}")
    resp = input("""
Enter the Scan option for the IP.
1. SYN ACK Scan
2. UDP Scan
3. Comprehensive Scan
4. ARP Scan 
5. Port , service , Os Scan 
6. Subdomain Finder
7. Password Crack n Keep
8. Exit\n""")
    
    if resp == "1":
        print ("Nmap Version : ", scan.nmap_version())
        scan.scan(ip_addr,'1-1024','-v -sS')
        print(scan.scaninfo())
        print("IP Status is ",scan[ip_addr].state())
        print ("Open Ports : ",list(scan[ip_addr]['tcp'].keys()))
    elif resp == "2":
        print ("Nmap Version : ", scan.nmap_version())
        scan.scan(ip_addr,'1-1024','-v  -sU')
        print(scan.scaninfo()) 
        print("IP Status is ",scan[ip_addr].state())
        print ("Open Ports : ",list(scan[ip_addr]['udp'].keys()))
    elif resp == "3":
        print ("Nmap Version : ", scan.nmap_version())
        #scan.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')
        # for x,y in nm.items():
        #   print(x,y)
        nm=scan.scan(ip_addr,'1-1024','-v -sS -sV -sC -A -O')["nmap"]
        print(scan.scanstats())
        print(scan.scaninfo())
        want= input("Do you want a detailed description (Yes/No): ")
        if want=='Yes' or want=='Y'or want=='y'or want=='yes': 
          pprint.pprint(nm["scan"])
        else:
          print("IP Status is ",scan[ip_addr].state())
          print("OS Name: ",scan[ip_addr].get('osmatch')[0]['name'])
          print ("Open Ports(TCP Stack) : ",list(scan[ip_addr]['tcp'].keys()))
    elif resp == "4":
        ip = input("Enter Default Gateway address : ") 
        scanner(ip+'/24')
    elif resp == "5":
        fingerprint.main1()
    
    elif resp=="6":
        subdomain_array = sd.SubDom()
        domain = input("Enter Domain whose subdomain is to be scanned : ")
        sd.subDomain_Scan(domain,subdomain_array)
    elif resp=="7":
        passwd.passwords()
    elif resp=="8":
        exit()
    else :
        print("Please enter valid response")
    
    # ip='192.168.29.1'+'/24' #Enter the defualt gateway IP address
    
    # scanner(ip)