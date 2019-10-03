class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j=target-i
            if j in nums: 
                if i != j:
                    return [nums.index(i),nums.index(j)]
                elif i == j and nums.count(i)>=2:
                    a=nums.index(i)
                    nums.remove(i)
                    b=nums.index(j)+1
                    return [a,b]
