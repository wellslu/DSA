# week5.Wednesday
- 課程內容
 
 1、今天先從編譯開始講起，編譯分四步驟，預處理->編譯->組裝->連結，預處理是指編譯器會將不執行不分轉成0處理部分為1，再來編譯會把程式語言轉成彙編語言，組裝的話就是將彙編語言轉成二進位，最後連結會把程序的0跟1和程式碼的0跟1做結合。
 
 <img src='http://cdn.cs50.net/2013/fall/lectures/5/w/notes5w/compiling.png' height=400 weight =400>
 
 2、先回憶上次講的跟節省記憶體有關的東西，那今天是要來驗證，正常來講要節省記憶體的話，記憶體的調用應該如下圖表示，當一個stack用完時應該被消除
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/1.jpg' height=200 weight =200>　<img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/2.jpg' height=200 weight =200>
 
 但很顯然的，教授給一個david/o的字串，執行結束後他仍然佔用記憶體的位置，
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/5.jpg' height=200 weight =200>
 
 所以在這之後教授給了一個程式碼free()，讓原本占用記憶體的stack在結束後被釋放了，
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/6.jpg' height=200 weight =200>
 
 下一個範例教授用了指向的方式做，照原本的方式講，指向一個是存放10個東西的chain時沒問題，但第11個東西進來的話呢?那就會回顧上周的，多餘的訊息就會往下放，造成內存洩露，
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/7.jpg' height=200 weight =200>
 
 所以就會像這樣，40bytes裡面每一格都掉一個出來，
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/3.jpg' height=200 weight =200>
 
 而如果攻擊者有心要攻擊你的電腦時，就會像這樣，把值拉大程式就會跑內存錯誤了，
 
 <img src='https://github.com/wellslu/DSA/blob/master/CS50/week5/jpg/4.jpg' height=200 weight =200>
 
 最後是圖片的儲存方式，最簡單的方式是以0是黑1是白來存取一張黑白圖，最後我不敢相信他們的作業看起來如此的難。
