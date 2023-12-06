import socket
import sys
import threading
#SERVER credentials

IP  = socket.gethostbyname(socket.gethostname())
PORT = 54321
#global variables
BUFFER = 1024
FORMAT = "UTF-8"
client_list = []
name_list = []

try:
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((IP,PORT))
    s.listen()
    print(f"server is listening for client at{IP}:{PORT}")
except socket.error as e:
    print(f"Error in socket cretion : {e} ")
    sys.exit()

def broadcast(msg):
    for c in client_list:
        c.send(msg.encode(FORMAT))

def client_handle():
    while True:
        try:
            msg = conn.recv(BUFFER).decode(FORMAT)
            broadcast(msg)
        except:
            index = client_list.index(conn)
            client_list.remove(conn)
            user_name = name_list[index]
            broadcast(f"{user_name} has left the chat")
            name_list.remove(user_name)
            break

while True:
    try:
        conn,addr = s.accept()
        print(f"(addr) connected with server")
        conn.send("uname".encode(FORMAT))
        uname = conn.recv(BUFFER).decode(FORMAT)
        client_list.append(conn)
        name_list.append(uname)
        broadcast(f"{uname} joined the chat")
        client_thread = threading.Thread(target=client_handle,args=(conn,))
        client_thread.start()
        active_connections = threading.active_count()-1
    except Exception as e:
        print(f"Error in crating a thread{e} ")
        break
    except KeyboardInterrupt:
        print("server is closed")
        break