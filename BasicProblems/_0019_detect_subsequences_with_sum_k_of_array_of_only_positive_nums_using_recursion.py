def detectSub(arr,target,i=0,total=0,result=[],sub=[]):
    if(i==len(arr)):
        return False
    
    sub.append(arr[i])
    total+=arr[i]
    if(target<=total):
        if(target==total):
            return True
        total-=arr[i]
        sub.pop()
        return False
    
    res1 = detectSub(arr,target,i+1,total,result,sub)
    total-=arr[i]
    sub.pop()

    res2 = detectSub(arr,target,i+1,total,result,sub)
    return res1 or res2


print(detectSub([1,2,3,4,5,6,7],50))
