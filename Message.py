import time
import os
import numpy as np






def SpecificWhatappMessage(reciverNumber,text):
    import pyautogui
    import pywhatkit
    message = pywhatkit.sendwhatmsg_instantly(reciverNumber,text,wait_time=65)
    time.sleep(60)
    pyautogui.press('enter')
    if not(bool(message)):
            print("Whatsapp Message Sent Sucessfully!\n\n")


def SpecificTextMessage(reciverNumber,text):
    import twilio.rest as twilio
    client=twilio.Client(os.getenv('twiliouser'),os.getenv('twiliopass'))
    message = client.messages.create(from_=os.getenv('twilionum'),body=text,to=reciverNumber)
    if message.sid:
        print("Message Sent Sucessfully!\n\n")



def WhatappMessage(reciverNumber):
    import pyautogui
    import pywhatkit
    text="Hi, LW Welcomes you"
    message = pywhatkit.sendwhatmsg_instantly(reciverNumber,text,wait_time=10,tab_close=True,close_time=3)
    time.sleep(60)
    pyautogui.press('enter')
    if not(bool(message)):
            print("Whatsapp Message Sent Sucessfully!\n\n")

def TextMessage(reciverNumber):
    import twilio.rest as twilio
    client=twilio.Client(os.getenv('twiliouser'),os.getenv('twiliopass'))
    text="Welcome to Pink City , Jaipur"
    message = client.messages.create(from_=os.getenv('twilionum'),body=text,to=reciverNumber)
    if message.sid:
        print("Message Sent Sucessfully!\n\n")


def message(data):  
    for i in data[:,3]:
        WhatappMessage("+91"+i)


def textMessage(data):
    city="Jaipur"
    for i in range(6):
        if data[i,1]!=city:
            TextMessage("+91"+data[i,3])