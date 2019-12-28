import subprocess
from getpass import getpass
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
    else:
        print("Invalid choice!")
