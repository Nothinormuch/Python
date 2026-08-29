from random import randrange
def quick_sort(arr, low_index, high_index):
    # print("Performing Quick Sort on:",arr[low_index:high_index+1])
    _len = high_index - low_index+1
    if _len <= 1:
        return arr
    
    pivot_index = randrange(low_index,high_index+1)
    # print("pivot:",pivot_index,"value: ",arr[pivot_index])
    
    arr[pivot_index], arr[low_index]=arr[low_index], arr[pivot_index]
    pivot_index = low_index
    # print("pivot:",pivot_index,"value: ",arr[pivot_index])
    
    i,j = low_index+1,high_index

    while(i<j):
        if(arr[i]>arr[pivot_index] and arr[j]<arr[pivot_index]):
            arr[i],arr[j] = arr[j],arr[i]
        if(arr[i]<=arr[pivot_index]):
            i+=1
        if(arr[j]>=arr[pivot_index]):
            j-=1

    if(arr[j]>arr[pivot_index]):
        arr[j-1],arr[pivot_index]=arr[pivot_index],arr[j-1]
        pivot_index = j-1
        # print("pivot:",pivot_index,"value: ",arr[pivot_index])
    else:
        arr[j],arr[pivot_index]=arr[pivot_index],arr[j]
        pivot_index = j
        # print("pivot:",pivot_index,"value: ",arr[pivot_index])

    quick_sort(arr,low_index,pivot_index-1)
    quick_sort(arr,pivot_index+1,high_index)

list = [9,5,5,5,8,7,6,5,4,3,2,5,5,5,1]
quick_sort(list,0,len(list)-1)
print(list)
