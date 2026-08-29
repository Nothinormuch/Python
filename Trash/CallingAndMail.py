import os


def get_purpose(searchCollege,data):
    for i in range(6):
        if data[i,2]==searchCollege:
            print("The Perpous of their life is : {}".format(data[i,4]))


def Calling(reciverNumber):
    from twilio.rest import Client
    client = Client(os.getenv('twiliouser'),os.getenv('twiliopass'))
    call = client.calls.create(to=reciverNumber,from_=os.getenv('twilionum'), url='https://drive.google.com/uc?export=download&id=16wAhwyzeXnrrw09WydQhLMR0-06gw5wz')
    if call.sid:
        print("Call Made Sucessfully!")



def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, app_specific_password):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    print("Message Made!")
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, app_specific_password)
        print("Logged in sucessfully! ")
        server.send_message(message)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    finally:
        server.quit()