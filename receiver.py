import os
import time

def listen_for_handshake():
    print("Waiting for handshake...")
    while True:
        response = os.popen("ping -c 1 -p 68616e647368616b65 192.168.190.148").read()
        if "bytes from" in response:
            print("Handshake received. Connected.")
            break
        time.sleep(1)

def receive_message():
    print("Receiving message...")
    message_hex = ""
    while True:
        response = os.popen("ping -c 1 192.168.190.148").read()
        if "bytes from" in response:
            data = response.split(" ")[-1].strip()
            if data:
                message_hex += data
        else:
            break
        time.sleep(1)

    message = bytes.fromhex(message_hex).decode('utf-8')
    print(f"Received message: {message}")

def main():
    listen_for_handshake()
    receive_message()

if __name__ == "__main__":
    main()
