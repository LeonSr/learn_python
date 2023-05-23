import socket
import requests

# Get the hostname and local IP address
hostname = socket.gethostname()
local_ip_address = socket.gethostbyname(hostname)

# Get the global IP address from ipinfo.io
response = requests.get("https://api.ipify.org")
global_ip_address = response.text.strip()

# Create a new text file and write the information to it
with open("test\\trash.txt", "w") as file:
    file.write("Hostname: " + hostname + "\n")
    file.write("Local IP Address: " + local_ip_address + "\n")
    file.write("Global IP Address: " + global_ip_address + "\n")

print("System information saved to system_info.txt file.")