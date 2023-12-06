import socket
import sys
import threading
#SERVER credentials

IP  = '10.10.145.158'
PORT = 54321
#global variables
BUFFER = 1024
FORMAT = "UTF-8"

username = input("Enter your user name : ")

try:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))
   
    print(f"connected with server")
except socket.error as e:
    print(f"Error in socket cretion : {e} ")
    sys.exit()

def recv_data():
    while True:
        try:
            msg  = s.recv(BUFFER).decode(FORMAT)
            if msg == "uname":
                s.send(username.encode(FORMAT))
            else:
                print(msg)
        except Exception as e:
            print(f"Error in recv message: {e}")
            s.close()
            break
    sys.exit()

def send_data():
    while True:
        try:
            msg = f"{username} >> {input('')}"
            s.send(msg.encode(FORMAT))
        except Exception as e:
            print(f"Error in send message: {e}")
            s.close()
            break
    sys.exit()

threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()