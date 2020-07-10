#Simple script for basic network configs
#Start Imports
import colorama
from colorama import Fore,Style

import csv

#Variables
NA = "N/A"

#Menu
def menu():
    print (Fore.GREEN) 
    print ("~~~Basic Networking Script~~~")
    print ("1. Pull running configs")
    print ("2. Configure access points")
    print ("3. Configure Cameras")
    print ("4. Configure Fiber ports")
    print ("5. Edit ZTP CSV template")
    print ("0. Exit")
print (Style.RESET_ALL)
  
loop=True      
            
while loop:
    menu()
    print (Fore.YELLOW)
    choice = int(input("Enter your choice [1-5]: "))
    print (Style.RESET_ALL)

     
#Pull Runnig Config
    if choice==1:     
        print ()
        print (Fore.YELLOW + "Paste these commands into the root of the switch:" + Style.RESET_ALL)
        print (Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("term len 0")
        print ("sh inv | i SN")
        print ("sh sw")
        print ("sh vl br")
        print ("sh int des")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("sh cdp ne det | i Dev|Interface|IP")
        print ("sh int status | i connected")
        print ("sh int status")
        print ("sh vtp st")
        print ("sh run")
        print ("term len 30")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (Style.RESET_ALL)
    
# Configure AP
    elif choice==2:
        range = str(input(Fore.YELLOW + 'Enter the range of interfaces (g1/0/1-12...):' + Style.RESET_ALL)).lower().strip()
        print (Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("interface " + range)
        print ("switchport trunk allowed vlan 1,2,212,215,217,240,254")
        print ("switchport trunk native vlan 2")
        print ("switchport mode trunk")
        print ("switchport noneg")
        print ("logging event trunk-status")
        print ("storm-control broadcast level 2.00")
        print ("storm-control multicast level 2.00")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (Style.RESET_ALL)
        
# Configure Cameras
    elif choice==3:
        print (Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        port = str(input(Fore.YELLOW + 'Enter the port of Camera (g1/0/12...):' + Style.RESET_ALL)).lower().strip()
        desc = str(input(Fore.YELLOW + 'Enter the description of camera(mac,ip,location):' + Style.RESET_ALL)).lower().strip()
        print (Fore.RED + "interface " + port)
        print ("description " + "<" + desc + ">")
        print ("switchport access vlan 250")
        print ("switchport mode access")
        print ("spanning-tree portfast edge")
        print ("switchport voice vlan 252")
        print ("switchport nonego")
        print ("no priority-queue out")
        print ("no mls qos trust dscp")
        print ("storm-control broadcast level 1.00")
        print ("storm-control multicast level 1.00")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (Style.RESET_ALL)

# Configure Fiber Ports       
    elif choice==4:
        print (Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1 GiG fiber:")
        print ("interface ra g1/0/49-50, g2/0/49-50, g3/0/49-50, etc")
        print ("switchport mode trunk")
        print ("switchport noneg")
        print ("logging event trunk-status")
        print ("ip dhcp snooping trust")
        print ("no shut")
        print ("exit")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("10 GIG Fiber:")
        print ("interface ra tenGigabitEthernet1/0/1-2, TenGigabitEthernet2/0/1-2, tenGigabitEthernet3/0/1-2")
        print ("description < Uplink to 6880 >")
        print ("switchport mode trunk")
        print ("logging event trunk-status")
        print ("no channel-group 1 mode active")
        print ("ip dhcp snooping trust")
        print ("no shut")
        print ("exit")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (Style.RESET_ALL)
        
    elif choice==5:
        print (Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        CSVname = str(input(Fore.YELLOW + 'Enter the name of the CSV File:' + Style.RESET_ALL)).strip()
        serial = str(input(Fore.YELLOW + 'Enter the Switch Serial number:' + Style.RESET_ALL)).strip()
        stk = str(input(Fore.YELLOW + 'Enter the stack module Serial number:' + Style.RESET_ALL)).strip()
        ass = str(input(Fore.YELLOW + 'Enter the Association name:' + Style.RESET_ALL)).strip()
        ip = str(input(Fore.YELLOW + 'Enter the vl2 ip address:' + Style.RESET_ALL)).strip()
        gateway = str(input(Fore.YELLOW + 'Enter the gateway:' + Style.RESET_ALL)).strip()
        host = str(input(Fore.YELLOW + 'Enter the Host name:' + Style.RESET_ALL)).strip()
        netmask = str(input(Fore.YELLOW + 'Enter the vl1 netmask:' + Style.RESET_ALL)).strip()
        vlan = str(input(Fore.YELLOW + 'Enter the access vlan:' + Style.RESET_ALL)).strip()
        VTP = str(input(Fore.YELLOW + 'Enter the VTP Domain:' + Style.RESET_ALL)).strip()
        print (Style.RESET_ALL)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (Style.RESET_ALL)
        
        with open(CSVname, mode='a') as csv_file:
            w = csv.writer(csv_file, quoting=csv.QUOTE_ALL) 
            w.writerow([serial, ass, serial, stk, NA, NA, NA, NA, ip, gateway, host, netmask, vlan, VTP])
            
    elif choice==0:
        loop=False
        print (Style.RESET_ALL)        
        
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")