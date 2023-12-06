import socket
import sys
import threading
import time
import datetime

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321
data_dict = {}
data_lock = threading.Lock()  # Lock to ensure thread-safe access to data_dict

def data_storage(client_adr, data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with data_lock:
        data_dict[client_adr] = {'data': data, 'timeStamp': timestamp}

def save_data_to_file():
    while True:
        with data_lock:
            with open("sensor.txt", "a") as file:
                for client_adr, data in data_dict.items():
                    file.write(f"{client_adr} >> {data['data']} (Timestamp: {data['timeStamp']})\n")
        time.sleep(5)  # Save data to the file every 5 seconds

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((IP, PORT))
        print(f"Server is up at {IP}:{PORT}")
    except socket.error as e:
        print(f"Error in socket creation: {e}")
        sys.exit()

    # Start the thread to periodically save data to the file
    save_thread = threading.Thread(target=save_data_to_file)
    save_thread.daemon = True
    save_thread.start()

    try:
        while True:
            data, client_adr = sock.recvfrom(1024)
            data_storage(client_adr, data.decode('utf-8'))
            print(f"{client_adr} >> {data.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exit")

    sock.close()

if __name__ == '__main__':
    main()
