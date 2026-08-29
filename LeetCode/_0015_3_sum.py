class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j, k = i+1, len(nums)-1
            while(j<k):
                sum = nums[i]+nums[j]+nums[k]
                if(sum==0):
                    result.append(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k+=1
                if(sum<0):
                    prev_j = j
                    j+=1
                    while(nums[prev_j]==nums[j]):
                        j+=1
                if(sum>0):
                    prev_k = k
                    k -= 1
                    while(nums[prev_k]==nums[k]):
                        k-=1
        return [list(i) for i in result]

print(Solution().threeSum([-1,0,1,2,-1,-4]))
