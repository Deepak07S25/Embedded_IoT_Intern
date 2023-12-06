import random
import socket
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321 # Replace with your server's port number
BUFFER = 1024
FORMAT = "utf-8"

def generate_sensor_data():
    return random.randint(0, 100)

def send_sensor_data(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data_to_send = str(data)
    client_socket.sendto(data_to_send.encode(FORMAT), (IP,PORT))
    client_socket.close()

if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data()  
        print("Sensor Reading:", sensor_data)
        send_sensor_data(sensor_data)  # Send the generated sensor data to the server

        time.sleep(10)  # Wait for 10 seconds before generating the next sensor data
