def quicksort(x):
    #先判斷要分類的數列中，數字有沒有超過兩個
    if len(x) >= 2:
        #以數列中第0個數當pivot，由此小的放左邊大的放右邊
        left = []
        right = []
        for i in x[1:]:
            if i < x[0]:
                left.append(i)
            else:
                right.append(i)
        #放完後將數列重整，並將左右兩邊的數列重複跑分類一次
        return quicksort(left)+[x[0]]+quicksort(right)
    #到最後數列只剩一個數的話會在這邊停下，並丟出最後一個數
    else:
        return x

if __name__ == '__main__':
	nums=[3,6,3,4,6,8,9,1,2,7,5]
	print(quicksort(nums))
