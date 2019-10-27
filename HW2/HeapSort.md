# HeapSort
把list轉成一個二元數，每一個二元樹有n/2個內部節點，以MaxHeapSort為例，先把list依照index位置轉成二元數後，每一個父節點下面最多有兩個子節點，當其中子節點比父節點大時，將其子節點與父節點交換，其父節點變為子節點後再與其下面的子節點做比較直到其節點比下面的子節點都還大，以此類推對所有節點都做一樣的事後，父節點會是list中最大的數，取出最大的數後再繼續比較父子節點。

時間複雜度:Best Case：Ο(n log n)    Worst Case：Ο(n log n)    Average Case：Ο(n log n)

- 將list轉成二元數:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/DataToHeap.png)

- 從下方開始檢查，若有子節點大於父節點的，則交換，並繼續往上面的父節點比較:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify03.png)
![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify04.png)

- 此時父節點跟子節點又有跟動，則再往下比較，直到父節點都大於下面的子節點:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify05.png)
![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify06.png)

參考網頁:http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php

# 學習歷程
- 1、上課時以先了解老師範例程式碼的MaxHeapSort是如何運行的，於是這次一樣秉持著原創的精神，我不但要用MinHeapSort寫，過程也會改寫成不同的方法。
- 2、範例程式碼中是跑了兩次的heapify，先做成一個最大二元樹，再依大小互換後將大的放到最後然後假裝不看，而我的作法傾向更簡單取出，只利用一個最小二元樹，把最小值放到最上面並利用pop()取出後，再繼續跑我的heapify。
- 3、我會保留老師for迴圈地從後到前，不是因為他寫的比較好，而是在我的fution中，我可以從後到前全部都跑到，所以可以確保最小的一定在最上面且寫法較簡單。
- 4、我在過程中，若遇到較小的就會直接先換，所以換的次數可能會比較多，而且我是寫到另一個list中，所以這可能會稍微影響到運行速度。

<img src='https://i.imgur.com/zJxhNe0.jpg' height=350 weight =700>

# 流程圖
![](https://i.imgur.com/ZwsUVKa.png)
