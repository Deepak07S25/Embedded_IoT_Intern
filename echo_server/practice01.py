import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321
#ye file bna kr store krne k liye usme data
def data_store(data):
    with open("sensor.txt","a") as file:
        file.write(data + "\n")
#bs ab socket bna kr bind kr do IP aur PORT se      
try:
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    soc.bind((IP,PORT))
    print(f"server is at {IP}:{PORT}")
except socket.error as e:
    print(f"Error in socket creation :{e}")
    sys.exit()
  # AB YEK WHILE LOOP SOCKET SE CONTINIOUS MESSAGE RECIEVE KR NE K LIYE
    
while True:
    try:
        msg,addr = soc.recvfrom(1024)
        print(f"{addr} >>{msg.decode('utf-8')}")
        
    except Exception as e:
        print(f"Error:{e}")
        break
    except KeyboardInterrupt:
        print("Exit")
        break
    sys.exit()   