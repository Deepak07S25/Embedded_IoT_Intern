import socket
import sys

IP = socket.gethostbyname (socket.gethostname())
PORT = 54321

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    print(f"client is ready")

except socket.error as e:
    print(f"ERROR in socket creation :{e}")
    sys.exit()
    
while True:
    try:
      msg = input(">> ")
      sock.sendto(msg.encode('utf-8'),(IP,PORT))
      
    except Exception as e:
        print(f"Error :{e}")
        break
    except KeyboardInterrupt:
        print("EXIT")
        break
sys.exit()