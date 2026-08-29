inputText=input("Enter a String: ")
checkList=[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,122)]+[chr(32),chr(33)]   #For Capitals, Smalls and ! and " "
# checkList=[chr(i) for i in range(97,122)]+[chr(32),chr(33)] #for only small alphabets and " " and !
prestring=""
for i in inputText:
    for j in checkList:
        print(prestring+j)
        if i==j:
            prestring+=i
            break

# inputText=input("Enter a String: ")
# print([ord(i) for i in inputText])