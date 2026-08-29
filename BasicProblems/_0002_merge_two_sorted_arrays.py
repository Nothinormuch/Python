def merge_arrays(left, right):
    len_left = len(left)
    len_right = len(right)
    i,j = 0,0
    result = []
    while(i < len_left and j < len_right):
        if(left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if(i<len_left):
        result.extend(left[i:])
    if(j<len_right):
        result.extend(right[j:])
    return result

