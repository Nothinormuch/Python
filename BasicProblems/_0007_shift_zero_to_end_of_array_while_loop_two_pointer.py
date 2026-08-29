def shift_zero(arr):
    _len=len(arr)
    i,j = 0,0
    while(j<_len):
        if(arr[j]!=0):
            arr[i]=arr[j]
            i+=1
        j+=1
    while(i<_len):
        arr[i]=0
        i+=1

arr = [1,2,9,0,0,0,1,0,1,0,0,1,0,0,0]

shift_zero(arr)

print(arr)
