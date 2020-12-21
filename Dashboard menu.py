#!/usr/bin/env python
"""
This is a python script that displays an option menu of the operations that you want to do.
"""

# IMPORTS
import rekenmachine, wachtwoord, ip_display, system_info_display, subprocess, time
import sys


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# CONFIGURING I/O


def dashboard():
    print("=" * 30, "Main Menu", "=" * 30)
    print("Select operation.")
    print("1. Rekenmachine")
    print("2. Wachtwoord")
    print("3. IP display")
    print("4. System info")
    print("5. Update system")
    print("6. Install software")
    print("7. EXIT")
    print("=" * 30, "End of the Menu", "=" * 24)

    keuze = input("Enter choice(1/2/3/4/5/6/8):\n")

    if keuze == '1':
        rekenmachine.main()     # Runs the program rekenmachine
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran the program rekenmachine
        dashboard()

    elif keuze == '2':
        wachtwoord.main()       # Runs the program wachtwoord
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran the program wachtwoord
        dashboard()

    elif keuze == '3':
        ip_display.main()       # Runs the program ip_display
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran the program ip_display
        dashboard()

    elif keuze =='4':
        system_info_display.main()  # Runs the program system_info_display
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran the program system_info
        dashboard()

    elif keuze == '5':
        subprocess.run('./update_system', shell=True)   # Update and upgrade your linux system
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran update_system
        dashboard()

    elif keuze == '6':
        subprocess.run('./software', shell=True)    # Begins the installation of the software
        time.sleep(2)           # Waits for 2 seconds to display the main menu after it ran install software
        dashboard()

    elif keuze == '7':                              # Exit the menu
        print("Goodbye")                            # Print goodbye
        sys.exit()
if __name__ == '__main__':  # code to execute if called from command-line
    dashboard()
