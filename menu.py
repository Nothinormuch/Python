from CallingAndMail import *
from CV2 import *
from InstagramAndParmiko import *
from Message import *
import dotenv
dotenv.load_dotenv()
data=np.array([['Rahul Sha','Jaipur','SL University','9667405524','Helping people'],
               ['Saddam Khan','Jaipur','ICFAI University','9667405524','Gaining Knowledge, happiness and sucess'],
               ['Sakshi Shukla','Lucknow','LPU','9667405524','to be sucessful'],
               ['Aditya Patil','Jaipur','Phulera','9667405524','To be a full stack dev'],
               ['Rahul Singhania','IFDC','','9667405524','Helping People'],
               ['Ravi Tiwari','Jaipur','Amity University','9667405524','Helping People']])

def main():
    choice=0
    while True:
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        print("|                       Menu                       |")
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        print("|1) Send Whatsapp Message to the numbers collected |")
        print("|2) Get Purpose                                    |")
        print("|3) Video Streaming                                |")
        print("|4) Paramkio                                       |")
        print("|5) Send Text Message to the people not from jaipur|")
        print("|6) Crop Pictures                                  |")
        print("|7) Calling                                        |")
        print("|8) Email                                          |")
        print("|9) Text message to a specific person              |")
        print("|10) Whatsapp message to a specific person          |")
        print("|11) Load Instagram comments                       |")
        print("|12) Exit                                          |")
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+\n")
        choice=int(input("Enter the option you want ot run: "))
        if choice==1:
            message(data)
        elif choice==2:
            searchCollege=input("Enter the name of the college to be searched for: ")
            get_purpose(searchCollege,data)
            input("Press Enter to continue:")
        elif choice==3:
            Frame()
        elif choice==4:
            paramiko_fun()
        elif choice==5:
            textMessage(data)
        elif choice==6:
            name=input("Enter the name of the person in frame: ")
            NewFrame(name)
        elif choice==7:
            countrycode=input("Enter the country code to send the message to: ")
            number=input("Enter the number to send the Call to: ")
            reciverNumber=countrycode+number
            if reciverNumber=="":
                reciverNumber=os.getenv('myphonenum')
            Calling(reciverNumber)
        elif choice==8:
            auto=input("auto: ")
            if auto=="":
                sender_email = os.getenv('mymail')
                receiver_email = os.getenv('mymail')
                subject = 'Test mail'
                body = 'This is a test email sent from Python.'
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                login = os.getenv('mymail')
                app_specific_password = os.getenv('apppass')
            else:
                sender_email = input("Enter the sender's mail: ")
                receiver_email = input("Enter the receiver's mail: ")
                subject = input("Enter the subject: ")
                body = input('Enter the body of the mail: \n\n')
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                login = input("Enter your login mail: ")
                app_specific_password = input("Enter the app specific password: ")
            
            send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, app_specific_password)
        elif choice==9:
            countrycode=input("Enter the country code to send the message to: ")
            number=input("Enter the number to send the message to: ")
            reciverNumber=countrycode+number
            text=input("Enter the message you want to send to {}:\n\n".format(reciverNumber))
            if reciverNumber=="":
                reciverNumber=os.getenv('myphonenum')
            SpecificTextMessage(reciverNumber,text)
        elif choice==10:
            countrycode=input("Enter the country code to send the message to: ")
            number=input("Enter the number to send the message to: ")
            reciverNumber=countrycode+number
            text=input("Enter the message you want to send to {}:\n\n".format(reciverNumber))
            if reciverNumber=="":
                reciverNumber=os.getenv('myphonenum')
            SpecificWhatappMessage(reciverNumber,text)
        elif choice == 11:
            post_url = input("Enter the url to the post: ")
            InstaLoadComment(post_url)
            input("Press Enter to continue:")
        elif choice==12:
            print("Exiting Program!")
            os.system("curl ascii.live/rick")
            break
        else: 
            print("You have entered an invalid choice! Please Retry.")


main()
