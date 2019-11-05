class Solution():
    def __init__(self):
        self.val = None  #最後要跑出的東西放這
    def mer(self,left,right):#每次merge的兩個list當左右
        if type(left) == int:#如果不為list就先轉成list，好在下面比較
            left = [left]
        if type(right) == int:
            right = [right]
        m = []#這是合併後的放這
        llen = len(left)#左右長度
        rlen = len(right)
        l = 0#從list0開始
        r = 0
        while l != llen and r != rlen:#當左右list任一長度到頂了，就停止迴圈
            if left[l] > right[r]:#如果左大於右，取那個數，並將左長度+1
                m.append(right[r])
                r+=1
            else:#反之則全相反
                m.append(left[l])
                l+=1
        if l == llen:#若左長度到頂了，代表左邊數用完了，那就將右邊剩下的數加回新list
            m = m + right[r:]
        elif r == rlen:#反之
            m = m + left[l:]
        return m

    def merge_sort(self,nums):
        self.val = nums[0]#取list中的第一個數，因為我是在list中包list
        l= len(nums)#總共有幾個list要兩兩合併
        i = 0#一樣從0開始
        if l != 1:#如果list中只有一個數代表是我最後的答案
            num = []#這是我每次整理後的整理後的答案
            while i+2 <= l:#如果list中還剩至少兩個數
                m = self.mer(nums[i],nums[i+1])#每兩個數merge sort排列
                num.append(m)#新的兩兩排列append到新整理後的答案中
                i+=2
            if l%2 != 0 and type(nums[-1]) == int:#如果有剩餘落單的一個，看他是不是int，是的話轉成list加回去答案list，不是的話直接加回去
                num.append([nums[-1]])
            elif l%2 != 0 and type(nums[-1]) == list:
                num.append(nums[-1])
            self.merge_sort(num)#重複這動作直到答案list中剩一個list
        return self.val
