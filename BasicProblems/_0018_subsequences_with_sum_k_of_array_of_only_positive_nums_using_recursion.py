def getSubs(arr,target,total=0,i=0,res=[],sub=[]):
    if(i==len(arr)-1):
        if(sum(tuple(sub))==target):
            res.append(sub.copy())
        return
    sub.append(arr[i])
    total+=arr[i]
    if(total>=target):
        if(total==target):
            res.append(sub.copy())
        total-=arr[i]
        sub.pop()
        return
    getSubs(arr,target,total,i+1,res,sub)
    sub.pop()
    total-=arr[i]
    getSubs(arr,target,total,i+1,res,sub)
    
    return res

print(getSubs([2,1,0,2,4],3))
    
