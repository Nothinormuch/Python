List=[1,6,17,3]
count = 0
while(count<len(List)):
    if List[count] == 17:
        count+=1
        continue
        print("here")
    print(List[count])
    count+=1