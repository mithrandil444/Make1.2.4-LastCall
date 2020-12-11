#!/usr/bin/env python
"""
This is a python script that displays your system info of your computer
"""

# IMPORTS
import platform


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# CONFIGURING I/O


def main():
    print("=" * 40, "System Information", "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
