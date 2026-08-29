import os
import re
import time

def send_ping(target_ip, message):
    for char in message:
        os.system(f'ping -n 1 {target_ip}')
        time.sleep(0.1)  # Delay to avoid flooding

def receive_ping():
    response = os.popen("ping -n 1 127.0.0.1").read()
    return "ping"

def handshake(target_ip):
    while True:
        os.system(f'ping -n 1 {target_ip}')
        response = os.popen("ping -n 1 127.0.0.1").read()
        if "Reply from" in response:
            print("Connected!")
            break
        time.sleep(1)

def wait_for_handshake():
    while True:
        response = os.popen("ping -n 1 127.0.0.1").read()
        if "Reply from" in response:
            print("Connected!")
            break
        print("Waiting for someone to connect...")
        time.sleep(1)

