def detectSub(arr,target,i=0,total=0,result=[],sub=[]):
    if(total == target):
        return True
    if(total>target):
        return False
    if(i==len(arr)):
        return False
    
    sub.append(arr[i])
    total+=arr[i]
    
    res1 = detectSub(arr,target,i+1,total,result,sub)
    if res1==True: return res1
    total-=arr[i]
    sub.pop()

    res2 = detectSub(arr,target,i+1,total,result,sub)
    return res2


print(detectSub([1,2,3,4,5,6,7],10))
