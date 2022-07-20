import sys
import socket
import time
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    print(":{}".format(sys.argv[1]))
    print ("IP {}".format(target))
else:
    print(" Error")
try:
    start = time.time()
    for port in range(1,30000):
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        willconnect = scan.connect_ex((target, port))
        if willconnect == 0:
            print("{} is open".format(port))
    scan.close()
    end = time.time()
    print(end - start)
except socket.error:
    print("Error")
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
        



#for connecting to port
#print("Running on Port {}".format(port))
#connec.connect(union)
#union = (sys.argv[1],port)

