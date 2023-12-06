
 
import socket
import sys
HOST = "192.168.43.2"
PORT = 54321  
BUFFER = 1024
FORMAT = 'utf-8'
#create socket and listen for clients
def create_socket():
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT)) 
       
        print(f"Connection established")
        return s 
       
    except socket.error as e:
        print(f"Error in creating socket :{e}")
        sys.exit()
    except KeyboardInterrupt:
        print("keyboard Interrput")
        sys.exit()
        
def send_recv(s):
    while True:
        try:
            s_msg = input(">> ")
            s.send(s_msg.encode(FORMAT))
            msg = s.recv(BUFFER)
            if not msg:
                print("no message from server")
                break
        except socket.error as e:
            print(f"Error in creating socket :{e}")
            sys.exit()
        except KeyboardInterrupt:
            print("keyboard Interrput")
            sys.exit()
        

if __name__ =="__main__":
    s=create_socket()
    send_recv(s)
