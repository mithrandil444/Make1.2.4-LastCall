#!/usr/bin/env python
"""
This is a python script that displays an option menu of the operations that you want to do.
"""

# IMPORTS
import rekenmachine, wachtwoord, ip_display, system_info_display, subprocess, time

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O


def dashboard():
    print("Select operation.")
    print("1. Rekenmachine")
    print("2. Wachtwoord")
    print("3. IP display")
    print("4. System info")
    print("5. Update system")
    keuze = input("Enter choice(1/2/3/4/5):\n")

    if keuze == '1':
        rekenmachine.main()     # Runs the programm rekenmachine
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran the program rekenmachine
        dashboard()

    elif keuze == '2':
        wachtwoord.main()
        time.sleep(2)
        dashboard()

    elif keuze == '3':
        ip_display.main()
        time.sleep(2)
        dashboard()

    elif keuze =='4':
        system_info_display.main()
        time.sleep(2)
        dashboard()

    elif keuze == '5':
        subprocess.call('./update_system')
        time.sleep(2)
        dashboard()

if __name__ == '__main__':  # code to execute if called from command-line
    dashboard()
