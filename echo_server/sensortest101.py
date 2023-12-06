import random
import time
   
IP = socket.gethostbyname (socket.gethostname())
PORT = 64321
BUFFER = 1024

def generate_sensor_data():
    return random.randint(0, 100)

def send_sensor_data(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.connect((IP,PORT))
    print("Connected to the server.")

    data_to_send = str(data)
    client_socket.send(data_to_send.encode(FORMAT))

    client_socket.close()




