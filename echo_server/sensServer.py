import socket
import sys
IP = socket.gethostbyname (socket.gethostname())
PORT = 54321  
BUFFER = 1024
FORMAT = "utf-8"

def store_sensor_data(data):
    with open("sensor_data.txt", "a") as file:
        file.write(data + "\n")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((IP,PORT))
    print(f"Server is listening for clients at {IP}:{PORT}")

    while True:
        data, client_address = server_socket.recvfrom(BUFFER)
        if not data:
            break

        sensor_data = data.decode(FORMAT)
        store_sensor_data(sensor_data)

        print(f"Received Sensor Reading from {client_address}: {sensor_data}")

if __name__ == "__main__":
    start_server()
