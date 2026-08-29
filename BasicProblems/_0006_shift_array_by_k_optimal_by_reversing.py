from _0005_reverse_array_swap_till_middle import reverse_array_slice as reverse

def shift_array_by_k(arr,k):
    _len = len(arr)

    k = k % _len

    reverse(arr,_len-k,_len-1)
    reverse(arr,0,_len-k-1)
    reverse(arr,0,_len-1)
    
    print(arr)

shift_array_by_k([1,2,3,4,5],6)
