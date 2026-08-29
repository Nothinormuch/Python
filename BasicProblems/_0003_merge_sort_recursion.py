from _0002_merge_two_sorted_arrays import merge_arrays

def merge_sort(arr):
    _len = len(arr)
    
    if (_len == 1):
        return arr

    mid_index = _len//2

    left_arr = merge_sort(arr[:mid_index])
    right_arr = merge_sort(arr[mid_index:])
    
    return(merge_arrays(left_arr,right_arr))


print(merge_sort([10,9,8,7,6,5,4,3,2,1]))
