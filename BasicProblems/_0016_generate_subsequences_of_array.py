def printSub(arr,i=0,tuple=[],sub=[]):
    if i == (len(arr)-1):
        sub.append(tuple.copy());
        return

    # Print
    tuple.append(arr[i])
    printSub(arr,i+1,tuple,sub)
    tuple.pop()
    
    # Not Print
    printSub(arr,i+1,tuple,sub)

    return sub

print(printSub([1,2,3,4])) 
