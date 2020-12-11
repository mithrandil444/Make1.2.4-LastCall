#!/usr/bin/env python
"""
This is a python script that gives a display of your IP-adress and the name of your computer.
"""

# IMPORTS
import socket

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# CONFIGURING I/O


def main():
        try:
            hostname = socket.gethostname()
            hostip = socket.gethostbyname(hostname)
            print("Hostname:  ", hostname)
            print("IP Address: ", hostip)
        except:
            print("Unable to get Hostname and IP")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
