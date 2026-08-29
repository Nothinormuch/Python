import os
import time

def send_handshake(target):
    os.system(f"ping -c 1 -p 68616e647368616b65 {target}")  # "handshake" in hex

def send_message(target, message):
    message_hex = message.encode().hex()
    chunks = [message_hex[i:i+32] for i in range(0, len(message_hex), 32)]
    
    for chunk in chunks:
        os.system(f"ping -c 1 -p {chunk} {target}")
        time.sleep(1)  # Small delay to avoid flooding

def main():
    target = input("Enter target IP: ")
    send_handshake(target)
    time.sleep(2)  # Wait for receiver to acknowledge
    message = input("Enter message: ")
    send_message(target, message)
    print("Message sent")

if __name__ == "__main__":
    main()
