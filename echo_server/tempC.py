import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(f"Error in socket creation: {e}")
        sys.exit()

    while True:
        try:
            data = input("Enter data to send to server (type 'exit' to quit): ")
            if data == 'exit':
                break

            data_bytes = data.encode('utf-8')
            sock.sendto(data_bytes, (IP, PORT))
        except Exception as e:
            print(f"Error: {e}")
            break

    sock.close()

if __name__ == '__main__':
    main()
