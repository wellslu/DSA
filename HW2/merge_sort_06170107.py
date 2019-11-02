class Solution():
    def __init__(self):
        self.val = None  
    def mer(self,left,right):
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]
        m = []
        llen = len(left)
        rlen = len(right)
        l = 0
        r = 0
        while l != llen and r != rlen:
            if left[l] > right[r]:
                m.append(right[r])
                r+=1
            else:
                m.append(left[l])
                l+=1
        if l == llen:
            m = m + right[r:]
        elif r == rlen:
            m = m + left[l:]
        return m

    def merge_sort(self,nums):
        self.val = nums[0]
        l= len(nums)
        i = 0
        if l != 1:
            num = []
            while i+2 <= l:
                m = self.mer(nums[i],nums[i+1])
                num.append(m)
                i+=2
            if l%2 != 0 and type(nums[-1]) == int:
                num.append([nums[-1]])
            elif l%2 != 0 and type(nums[-1]) == list:
                num.append(nums[-1])
            self.merge_sort(num)
        return self.val