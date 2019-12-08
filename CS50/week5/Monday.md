# week5.Monday
- 課程內容
 1、前10分鐘左右我先是對於那個教授感到敬佩，因為它可以邊上課邊打出他要的東西而且沒錯，但這部分我認為翻譯的有些不是很好加上我英文不好的關係有些不明白，但據我了解他先是用一個小遊戲來表示何謂他的上帝視角，只要下面的盤子不斷跟著球移動就永遠不會結束，從這邊帶入你看到的只不過是表面，而背後的東西在這堂課可以學到，並用一部電影當CGI和電腦科學的示範。
2、後面的部分，教授從sting和char開始講起，然後進入到linked list存放方式的講解，由於教授是用C來教課，我個人這次就沒有實做一遍了，主要我比較印象深刻的是他講解完swap後，他畫了用一般方式做和用linked list做時記憶體是如何運行的，你只需要記住的是位置，而不是一個實體，並且善用指向，就能輕鬆地省下記憶體空間，並且如果是有出現重複的情況，何不指向同一位置就好了呢?

array:　　　　　　　　　　　　　　　　linked list:

<img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/1575805346067.jpg' height=200 weight =200>　　<img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/1575805374024.jpg' height=200 weight =200>

然後再用一個不是當用法的例子來講解，每一個變數都需要一個指向的位置，但若沒提供會導致指不到對的地方，就需要修正

<img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/157.jpg' height=400 weight =400>
                                                                      
再來他提供一個維基百科上關於記憶體溢出的例子，若以傳統型方式存取的話可能就會導致當攻擊者有意侵入你的電腦時，不斷地塞滿你的記憶體，而你的記憶體不足卻需要存放傳來的東西時，超出容量的訊息會繼續往下放，造成有心人士就可以從這裡走到你電腦的main，進而奪取更高的權限。

<img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Stack_Overflow_4.png' height=400 weight =200>

所以如果以linked list方式來存放資料的話，以後要以這種手段來侵入你的程式時，就會變成這樣

<img src='https://imgs.xkcd.com/comics/pointers.png' height=400 weight =400>

最後附上一張記憶體的模樣

<img src='http://cdn.cs50.net/2013/fall/lectures/5/m/notes5m/program_memory.png' height=400 weight =200>

*課程:https://www.youtube.com/watch?v=IEuvKVjw2oM*
