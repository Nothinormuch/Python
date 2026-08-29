def merge_arrays(left,right):
    result = []
    l,r,i = 0,0,0
    if(left[l]<right[r]):
        result.append(left[l])
        l+=1
    else:
        result.append(right[r])
        r+=1
    while(l<len(left) and r<len(right)):
        if(left[l]<right[r]):
            if left[l]!=result[i]:
                result.append(left[l])
                i+=1
            l+=1
        else:
            if right[r]!=result[i]:
                result.append(right[r])
                i+=1
            r+=1
    while(l<len(left)):
        if left[l]!=result[i]:
            result.append(left[l])
            i+=1
        l+=1
    while(r<len(right)):
        if right[r]!=result[i]:
            result.append(right[r])
            i+=1
        r+=1
    print(result)

merge_arrays([1,2,2,2,2,3,4,4,4,4],[1,2,2,2,2,2,3,4,9,9,9,9,9])
