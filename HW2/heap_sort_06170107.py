class solution():
    def heap_sort(self, nums):
        a=len(nums)#先算出list長度
        y=[]#這個list是一個一個取出來時裝在這裡
        for i in range(a):#list有幾個數就取幾次
            for j in range(len(nums),-1,-1):#跑原本list裡面的數，從尾巴開始跑
                try:#由於list可能會超過，避免錯誤直接try它
                    if nums[j]>nums[2*j+1]:#開始每個節點比大小換位
                        nums[j],nums[2*j+1] = nums[2*j+1],nums[j]
                    if nums[j]>nums[2*j+2]:
                        nums[j],nums[2*j+2] = nums[2*j+2],nums[j]
                except:#若index超過，直接泡下一次迴圈
                    continue
            y.append(nums.pop(0))#每把最小值跑到最前面時，取出一次
        return y
