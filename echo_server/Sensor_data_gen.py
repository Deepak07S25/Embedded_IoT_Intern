import socket
import sys
import random

import time

IP = '10.10.146.35'
PORT = 54321

try:
    so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print(f"client is ready")
except socket.error as e:
    print(f"Error in socket creation : {e}")
    sys.exit()
    
while True:
    try:
        value = random.randint(1,100)
       # print(value)
        time.sleep(10)
        msg = str(value)
        print(f"message :{msg}")
        so.sendto(msg.encode('utf-8'),(IP,PORT))
    except Exception as e:
        print(f"Error : {e}")
        break
    except KeyboardInterrupt:
        print("Exit")
        break
sys.exit()