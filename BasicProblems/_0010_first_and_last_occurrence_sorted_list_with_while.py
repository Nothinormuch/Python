def first_and_last(nums: List[int],target: int) -> List[int]:
    _len = len(nums)
    
    l,r = 0, _len-1

    first = -1

    while(l<=r):
        mid = (l+r)//2
        if nums[mid] == target:
            r = mid - 1
            first = mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    l,r = 0, _len-1

    last = -1

    while(l<=r):
        mid = (l+r)//2
        if nums[mid] == target:
            l = mid + 1
            last = mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return [first,last]

print(first_and_last([1,2,3,4,5,5,5,5,5,6,7],1))
