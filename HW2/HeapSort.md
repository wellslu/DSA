# HeapSort
把list轉成一個二元數，每一個二元樹有n/2個內部節點，以MaxHeapSort為例，先把list依照index位置轉成二元數後，每一個父節點下面最多有兩個子節點，當其中子節點比父節點大時，將其子節點與父節點交換，其父節點變為子節點後再與其下面的子節點做比較直到其節點比下面的子節點都還大，以此類推對所有節點都做一樣的事後，父節點會是list中最大的數，取出最大的數後再繼續比較父子節點。

- 將list轉成二元數:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/DataToHeap.png)

- 從下方開始檢查，若有子節點大於父節點的，則交換，並繼續往上面的父節點比較:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify03.png)
![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify04.png)

- 此時父節點跟子節點又有跟動，則再往下比較，直到父節點都大於下面的子節點:

![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify05.png)
![](http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/img/Heapify06.png)

參考網頁:http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php
