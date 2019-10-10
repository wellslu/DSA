class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >= 2:
            left = []
            right = []
            for i in nums[1:]:
                if i < nums[0]:
                    left.append(i)
                else:
                    right.append(i)
            return self.sortArray(left)+[nums[0]]+self.sortArray(right)
        else:
            return nums
