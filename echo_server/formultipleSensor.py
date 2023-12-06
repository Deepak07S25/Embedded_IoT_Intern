import socket
import sys
import threading
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321
#now here we are initializing dictionary
data_dict = {}

def data_storage(client_adr,data):
    data_dict[client_adr] = {'data':data, 'timeStamp': time.time()}
    
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print(f"server is at {IP}:{PORT}")
except socket.error as e:
    print(f"Error in socket crearition : {e}")
    sys.exit()
    
while True:
    try:
        data,client_adr = sock.recvfrom(1024)
#now we are going to add data int data storage function along with time

        data_storage(client_adr,data.decode('utf-8'))
    except Exception as e:
        print(f"error is as {e}")
        break 
    except KeyboardInterrupt:
        print("Exit")
        break
sock.close()
sys.exit()
    