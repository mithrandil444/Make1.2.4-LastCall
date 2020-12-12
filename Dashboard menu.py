#!/usr/bin/env python
"""
Info about our project comes here
"""

# IMPORTS
import rekenmachine, wachtwoord, ip_display, system_info_display

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O
print("Select operation.")
print("1. Rekenmachine")
print("2. Wachtwoord")
print("3. IP display")
print("4. System info")

def main():
    keuze = input("Enter choice(1/2/3/4):\n")

    if keuze == '1':
        rekenmachine.main()


    elif keuze == '2':
        wachtwoord.main()

    elif keuze == '3':
        ip_display.main()

    elif keuze =='4':
        system_info_display.main()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
