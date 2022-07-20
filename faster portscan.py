import sys
import socket
import time
import concurrent.futures
allports = list(range(1,65536))

target = socket.gethostbyname(sys.argv[1])
if len(sys.argv) == 2:
    print(":{}".format(sys.argv[1]))
    print ("IP {}".format(target))
else:
    print(" Error")

def portscanner(port):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    willconnect = scan.connect_ex((target, port))
    if willconnect == 0:
        print("{} is open".format(port))
        scan.close()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(portscanner,allports)



# except socket.error:
#     print("Error")
#     sys.exit()
# except KeyboardInterrupt:
#     sys.exit()

#     pass
