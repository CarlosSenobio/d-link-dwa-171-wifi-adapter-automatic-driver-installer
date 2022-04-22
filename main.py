from aifc import Error
import os, re, webbrowser, time
from colorama import Fore, init, Back
# importing libs


def commands():
    terminal_commands = ["sudo apt update",
                    "sudo apt install build-essential git dkms",
                    "chmod +x dkms-install.sh",
                    "sudo ./dkms-install.sh",
                    "sudo modprobe 8821cu"
                    ]

    for command in terminal_commands:
        os.system(command)

# function for execute to the commmands

init(autoreset=True)
print("D-Link DWA 171 WIFI ADAPTER AUTOMATIC DRIVER INSTALLER")
print(Fore.RED + "Works only on Debian distros")
time.sleep(3)

# finding some dependencies

item = os.popen("apt list").read()
find = re.search("git-all", item)
print("Checking for dependencies...")

if find:
    try:
        print(Fore.GREEN + "OK")
        print("No dependency found\n")
        os.system("git clone https://github.com/brektrou/rtl8821CU.git")
        os.chdir("rtl8821CU")
        time.sleep(1)
        commands()
        print(Fore.GREEN + "Drivers installed successfully")
    except  TypeError:
        print(f"Error: {Error}")
        exit()

else:
    # If any dependencies were found and not downloaded in the terminal, you will be directed to the website of the missing package
    print(Fore.RED + "Dependency found!")
    print("We'll download it for you!\n")
    time.sleep(1)
    download_git = os.system("sudo apt install git -y")
    
    if download_git == 25600:
        print("Package not found, you will be directed to the website...")
        webbrowser.open("https://git-scm.com/downloads")
        print(Fore.YELLOW + "Please restart the script")
        exit()
    else:  
        print(Fore.GREEN + "Drivers installed successfully")