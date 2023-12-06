import socket 
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321
def data_storage(data):
    with open("button_Press.txt","a") as file:
        file.write(data + "\n")

    
        
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((IP,PORT))
    print(f"server is up at {IP}:{PORT}")
except socket.error as e:
    print(f"Error in socket creation : {e}")
    sys.exit()
    
while True:
    try:
        msg, addr = sock.recvfrom(1024)
        print(f"{addr} >> {msg.decode('utf-8')}")
       
        data_storage(msg.decode('utf-8'))
    except Exception as e:
        print(f"Error : {e}")
        break
    except KeyboardInterrupt:
        print("Exit")
        break
sys.exit()