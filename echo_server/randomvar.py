import socket
import random
import time

SERVER_IP = socket.gethostbyname (socket.gethostname())
SERVER_PORT = 54321  # Replace with the server's port number
BUFFER = 1024
FORMAT = "utf-8"

def send_sensor_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to server.")

    while True:
        # Generate random sensor data (an integer between 0 and 100)
        sensor_data = random.randint(0, 100)
        data_to_send = str(sensor_data)

        # Send the data to the server
        client_socket.send(data_to_send.encode(FORMAT))
        print(f"Sent data: {data_to_send}")

        time.sleep(10)  # Wait for 10 seconds before sending the next data

    client_socket.close()

if __name__ == "__main__":
    send_sensor_data()

