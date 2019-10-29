class solution():
    def heap_sort(self, nums):
        a=len(nums)
        y=[]
        for i in range(a):
            for j in range(len(nums),-1,-1):
                try:
                    if nums[j]>nums[2*j+1]:
                        nums[j],nums[2*j+1] = nums[2*j+1],nums[j]
                    if nums[j]>nums[2*j+2]:
                        nums[j],nums[2*j+2] = nums[2*j+2],nums[j]
                except:
                    continue
            y.append(nums.pop(0))
        return y
