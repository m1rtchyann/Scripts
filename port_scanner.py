#!/usr/bin/env python3
import socket
import re # regular expressions to ensure that the input is correctly formatted.
from termcolor import cprint, colored

# Regular Expression Pattern to recognise IPv4 addresses.
# ^ - the start of string
# ?: - groups the pattern inside
# \d{1,3} - matches one to three digits
# \. - dot. Since dot is a special character, it needs to be escaped with a backslash (\) to match a literal dot
# {3} - means that what is written in the parentheses should be 3 more times
# $ - the end of string
ip_add_pattern = re.compile("^(?:\d{1,3}\.){3}\d{1,3}$")

# Regular Expression Pattern to extract the number of ports you want to scan.
port_range_pattern = re.compile("(\d+)-(\d+)")

port_min = 0
port_max = 65535
open_ports = []

cprint("WELCOME TO OUR NETWORK MAPPER", "green", attrs=["bold"])
while True:
    ip_addr = input("\nEnter the IP address you want to scan: ")
    if ip_add_pattern.search(ip_addr):
        # Additional check to ensure each number in the IP address is less than 256
        ip_numbers = map(int, ip_addr.split('.'))
        if all(0 <= num <= 255 for num in ip_numbers):
            break
        else:
            cprint("One or more numbers in the IP address are not in the range [0, 255]. Please enter a valid IP address.", "red")
    else:
        cprint("It's not a valid IP address.", "red")

while True:
    print("Please enter the range of ports you want to scan in format: int-int")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:
        # Create a socket object
        # AF_INET indicates that the socket can be used to communicate with IPv4 addresses.
        # SOCK_STREAM specifies that the socket will use TCP for communication.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set timeout for the socket to try and connect to the server.
            s.settimeout(0.5)
            # Connect to the ip address we entered and the port number.
            # If it can't connect to this socket the open_ports list won't append the value.
            s.connect((ip_addr, port))
            open_ports.append(port)
    except:
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_addr}.")