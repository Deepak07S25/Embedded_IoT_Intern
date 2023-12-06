#first task is to create socket
#then we will bind and listen and then accept data received also send| for client
 
import socket
import sys
HOST = socket.gethostbyname(socket.gethostname())
PORT = 55493   #can use ports above 25000\
BUFFER = 1024
FORMAT = 'utf-8'

#function to create socket and listen for clients
def create_socket():
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((HOST,PORT)) #socket ban gya bind ho gya port k sath
        s.listen()
        print(f"Server is listening clients at {HOST}:{PORT}")
        return s #taking socket as return
       
    except socket.error as e:
        print(f"Error in creating socket :{e}")
        sys.exit()
    except KeyboardInterrupt:
        print("keyboard Interrput")
        sys.exit()
        
def handle_client(s):
    while True:
        try:
            client, addr = s.accept()
            print(f"Client connected from{addr[0]} : {addr[1]}")
            while True:
                msg = client.recv(BUFFER)
                if not msg:
                    print("No msg  from client")
                    break
                print(msg)
                client.send(msg)
        except socket.error as e:
            print(f"Error in creating socket :{e}")
            sys.exit()
        except KeyboardInterrupt:
            print("keyboard Interrput")
            sys.exit()
        

if __name__ =="__main__":
    s=create_socket()
    handle_client(s)