# LinkedList
- 邏輯概念 : 從頭開始為第一個節點，每一個節點內存著資料以及通往下一個節點的道路，以此類推把所有資料以道路連接起來就是linkedlist。
- 用意 : linkedlist是以節點的形式將資料串連，好處是可以比array更節省資料的儲存空間，因為可以在各個儲存處取出少量空間來儲存任意節點的單一資料，但缺點就是再取資料時需要從第一個開始走到需要的資料存放處，速度相對較array慢。

![](https://s3.amazonaws.com/hr-challenge-images/17168/1456961238-28488bfa0d-LinkedListExplanation.png)

# Stack
- 邏輯概念 : 將新節點像盤子裝在容器一樣堆疊上去，每增加新節點都只能從最上面往上加，要取出時也只能從最上面的取出。
- 用意 : 將linkedlist的功能簡化，使運行速度更快一些，用在特定工作上，如回復功能。
![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Lifo_stack.png/350px-Lifo_stack.png)

# Queue
- 邏輯概念 : Queue就像是排隊一樣，一個人就是一個節點，新增的節電要從最後面開始排，要取出節點也是最前面的優先取出。
- 用意 : 與stack相同，簡化linkedlist功能，用於特定工作上，如印表機工作排序。
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Fifo_queue.png/350px-Fifo_queue.png)
