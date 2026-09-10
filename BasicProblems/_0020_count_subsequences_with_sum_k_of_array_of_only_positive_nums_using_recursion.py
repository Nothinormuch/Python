def detectSub(arr,target,i=0,total=0,result=[]):
    if(total == target):
        return 1
    if(total>target):
        return 0
    if(i==len(arr)):
        return 0
    
    total+=arr[i]
    res1 = detectSub(arr,target,i+1,total,result)
    total-=arr[i]

    res2 = detectSub(arr,target,i+1,total,result)
    return res1+res2


print(detectSub([1,2,3,4,5,6,7],20))
