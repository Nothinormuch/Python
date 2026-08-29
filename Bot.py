inputFile = "D:\my stuff\refrences\Vasudha\Linefindingbot\Source.txt"
givenString = input("Enter a solution: ")
print('The following lines contain your solution {', givenString, '}:')
Source=["Built greenhouse","Use 3 Rs","No plastic","stop foodwastage","no polution","use solor powered greenhouse","Use solar pannels as an alternative for windmills","use windmills"]
points=0
for line in Source:
      
      if givenString in line:
         print(line)
         points=points+1
if points == 0:
    print("your solution quiet unique hence it is send to the admin who will check it and give you your reward accordingly!","Congrats",sep="\n")
else:
    print ("Your Solution recives",points,"points","Better luck next time",sep="\n")