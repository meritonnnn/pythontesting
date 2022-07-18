#!/usr/bin/env python

from tracemalloc import start
from sys import platform
import os
from subprocess import Popen
from subprocess import call

option = ""

def banner():
    return ("""

    ██████╗░███████╗███╗░░██╗██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗
    ██╔══██╗██╔════╝████╗░██║██║░░░██║██║██╔══██╗██║░░░██║██╔════╝
    ██████╦╝█████╗░░██╔██╗██║╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░
    ██╔══██╗██╔══╝░░██║╚████║░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗
    ██████╦╝███████╗██║░╚███║░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝
    ╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░

    """)

def menu():
    return ("""ENTER 0 - 13 TO SELECT OPTIONS

    1.  IP                           Enumerate  information  from  IP Address
    2.  DOMAIN                       Gather  information  about  given DOMAIN
    3.  PHONENUMBER                  Gather  information  about   Phonenumber
    4.  DNS MAP                      Map DNS  records associated  with target
    5.  METADATA                     Extract all metadata of  the  given file
    6.  REVERSE IMAGE SEARCH         Obtain domain name or IP address mapping
    7.  HONEYPOT                     Check if it's honeypot or a real  system
    8.  MAC ADDRESS LOOKUP           Obtain information about give Macaddress
    9.  IPHEATMAP                    Draw  out  heatmap  of  locations  of IP
    10. TORRENT                      Gather torrent download  history  of  IP
    11. USERNAME                     Extract Account info. from social  media
    12. IP2PROXY                     Check whether  IP  uses  any VPN / PROXY
    13. MAIL BREACH                  Checks given domain  has  breached  Mail
    99. UPDATE                       Update ReconSpider to its latest version

    0. EXIT                         Exit from the  BenVirus  to your terminal
    """)

def start_of_program():
    if platform == "linux" or platform == "linux2":
        pass
    elif platform == "darwin":
        pass
    elif platform == "win32":
        pass
    if platform == "darwin":
       pass
    else:
        print("You are not using the required operating system.")
        quit()

    global option
    print(banner())
    print(menu())
    option = input("Enter option: ")

start_of_program()

if option == "1":
    print("You have chosen option 1")
    print(menu())

elif option == "2":
    print("You have chosen option 2")
    print(menu())

elif option == "3":
    print("You have chosen option 3")
    print(menu())

elif option == "4":
    print("You have chosen option 4")
    print(menu())

elif option == "5":
    print("You have chosen option 5")
    print(menu())

elif option == "6":
    print("You have chosen option 6")
    print(menu())

elif option == "7":
    print("You have chosen option 7")
    print(menu())

elif option == "8":
    print("You have chosen option 8")
    print(menu())

elif option == "9":
    print("You have chosen option 9")
    print(menu())

elif option == "10":
    print("You have chosen option 10")
    print(menu())

elif option == "11":
    print("You have chosen option 11")
    print(menu())

elif option == "12":
    print("You have chosen option 12")
    print(menu())

elif option == "13":
    print("You have chosen option 13")
    print(menu())

elif option == "99":
    print("You have chosen option 99")
    call(["python3", "restart.py"])
    
    print(menu())

elif option == "0":
    quit()

else:
    print("You have not entered a valid option...")
    start_of_program()