import socket
import subprocess
from _datetime import datetime

target = input("Enter the target ip address")

def port_scanner(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"scanning the target {ip}")
        print("Time started: ", datetime.now())

        for port in range(20,90):
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(1)
          result = sock.connect_ex((ip, port))
          if result == 0:
              print("port {} Open".format(port))
          sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved")

    except socket.error:
        print("could not connet to the server")



port_scanner(target)