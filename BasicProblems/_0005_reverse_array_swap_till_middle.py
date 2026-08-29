def reverse_array_slice(arr,left_index,right_index):
    _len = right_index-left_index+1
    for i in range(_len//2):
        arr[left_index+i],arr[right_index-i]=arr[right_index-i],arr[left_index+i]

def reverse_array(arr):
    _len = len(arr)
    reverse_array_slice(arr,0,_len-1)
    print(arr)
