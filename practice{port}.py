import subprocess
import socket
from datetime import datetime
target = input("What's the target ip: ")
def port_scanner(target):
    try:

        ip = socket.gethostbyname(target)
        print(f"scanning the the target: {ip}")
        print("time started", datetime.now())

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print("port open {}".format(port))
                sock.close()

    except socket.gaierror:
        print("the target ip could not be resolved")
    except socket.error:
        print("Error")


port_scanner(target)





