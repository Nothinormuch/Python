def floor_and_ceil(nums, target):
    _len = len(nums)
    
    if nums == []:
        return [-1,-1]

    l,r = 0, _len-1
    floor = -1

    while(l<=r):
        mid = (l+r)//2
        if nums[mid] <= target:
            floor = mid
            l = mid + 1
        else:
            r = mid - 1

    

    l,r = 0, _len-1
    ceil = -1

    while(l<=r):
        mid = (l+r)//2
        if nums[mid] >= target:
            ceil = mid
            r = mid - 1
        else:
            l = mid + 1

    return [-1 if floor == -1 else nums[floor],-1 if ceil == -1 else nums[ceil]]

print(floor_and_ceil([1,2,4,5],10))
