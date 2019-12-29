import subprocess
from shlex import split
from getpass import getpass
from shutil import which
from sys import exit
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.OKBLUE)
print("                               _  __ _ ")
print("                              (_)/ _(_)")
print("  ___  __ _ ___ _   ___      ___| |_ _ ")
print(" / _ \/ _` / __| | | \ \ /\ / / |  _| |")
print("|  __/ (_| \__ \ |_| |\ V  V /| | | | |")
print(" \___|\__,_|___/\__, | \_/\_/ |_|_| |_|")
print("                 __/ |                 ")
print("                |___/                  ")
print(bcolors.ENDC)
if which("nmcli") is None:
    print(bcolors.FAIL+"easywifi requires NetworkManager, please install it before using this!"+bcolors.ENDC)
    exit()
def getssid(netname):
    p1 = subprocess.Popen(split("nmcli --fields NAME,UUID c"), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(split("grep -i "+str(netname)), stdin=p1.stdout, stdout=subprocess.PIPE)
    ss=p2.communicate()[0].decode('utf-8')
    return str(ss.split()[1])
while True:
    print("\n")
    print("=======================================")
    print("                  MENU                 ")
    print("=======================================")
    print("1) Scan for networks")
    print("2) List my devices")
    print("3) List saved networks")
    print("4) Connect to a saved network") #known and unknown
    print("5) Setup new network")
    print("6) Create a hotspot")
    print("7) Remove a saved network")
    print("8) Takedown hotspot")
    print("\n")
    choice = input(": ")
    if choice == "1":
        result = subprocess.run(['nmcli', "d", "wifi", "list"], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))    
    elif choice == "2":
        result = subprocess.run(['nmcli', "d"], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif choice == "3":
        result = subprocess.run(['nmcli', "c"], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif choice == "4":
        network = input("Network: ")
        result = subprocess.run(['nmcli', "d", "wifi", "connect", network], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif choice == "5":
        network = input("Network: ")
        password = getpass()
        result = subprocess.run(['nmcli', "d", "wifi", "connect", network, "password", str(password)], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    elif choice == "6":
        if which("dnsmasq") is None:
            print(bcolors.FAIL+"creating hotspots requires dnsmasq, please install it before using this!"+bcolors.ENDC)
            continue
        result = subprocess.run(['nmcli', "d"], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        intf = input("Interface: ")
        hotspotname = input("Hotspot name: ")
        hotspotpass = getpass()
        step1 = subprocess.run(["nmcli","con","add","type","wifi","ifname",str(intf), "con-name",str(hotspotname),"autoconnect", "yes", "ssid", str(hotspotname)], stdout=subprocess.PIPE)
        print(step1.stdout.decode('utf-8'))
        step2 = subprocess.run(["nmcli","con","modify",str(hotspotname),"802-11-wireless.mode","ap","802-11-wireless.band","bg","ipv4.method", "shared"], stdout=subprocess.PIPE)
        print(step2.stdout.decode('utf-8'))
        step3 = subprocess.run(["nmcli","con","modify",str(hotspotname),"wifi-sec.key-mgmt","wpa-psk"], stdout=subprocess.PIPE)
        print(step3.stdout.decode('utf-8'))
        step4 = subprocess.run(["nmcli","con","modify",str(hotspotname),"wifi-sec.psk","'"+str(hotspotpass)+"'"], stdout=subprocess.PIPE)
        print(step4.stdout.decode('utf-8'))
        step5 = subprocess.run(["nmcli","con","up","uuid",getssid(hotspotname)], stdout=subprocess.PIPE)
        print(step5.stdout.decode('utf-8'))
    elif choice == "7":
        result = subprocess.run(['nmcli', "c"], stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
        contodel = str(input("Delete: "))
        result2 = subprocess.run(['nmcli', "connection", "delete", contodel], stdout=subprocess.PIPE)
        print(result2.stdout.decode('utf-8'))
    elif choice == "8":
        nn = str(input("Hotspot Name: "))
        step5 = subprocess.run(["nmcli","con","down",nn], stdout=subprocess.PIPE)
        print(step5.stdout.decode('utf-8'))
    else:
        print("Invalid choice!")
