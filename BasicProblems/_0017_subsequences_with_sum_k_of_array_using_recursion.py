def getSubs(arr,target,i=0,res=[],sub=[]):
    if(i==len(arr)-1):
        if(sum(tuple(sub))==target):
            res.append(sub.copy())
        return
    sub.append(arr[i])
    getSubs(arr,target,i+1,res,sub)
    sub.pop()
    getSubs(arr,target,i+1,res,sub)
    
    return res

print(getSubs([-1,2,1,0,2,4],3))
    
