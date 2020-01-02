# GA API
我的GA API學習過程都是從GA學習手冊上學習的https://developers.google.com/analytics/devguides/reporting/core/v4 https://developers.google.com/analytics/devguides/reporting/core/v3

GA說明中心https://support.google.com/analytics#topic=3544906
- 什麼是GA
  - 凡是 Analytics (分析) 使用者都可以使用下列三種 API：
  - 1、收集 API：可讓您自訂標準追蹤以外的追蹤程式碼，以便收集網站上的購買相關資料、在同一個檢視中取得兩個子網域的報表、設定自己的訪客類型定義等。
  - 2、管理 API：Analytics (分析) 管理 API 可讓您以 Google 資料 API 資訊提供格式快速存取 Analytics (分析) 帳戶和檢視資料。透過管理 API，您可以快速  取得與某個使用者相關的檢視組合，或是與特定檢視相關的目標設定資料。然後，您可以使用管理 API 搭配匯出 API，在報表中列出所需的資料。
  - 3、資料匯出 API：可讓您使用 Analytics (分析) 帳戶內現有的資料來製作應用程式。此類應用程式可透過 API 向現有的 Analytics (分析) 檢視要求報表層級的資料 (但必須先獲得該檢視的存取權)，並針對所選檢視擷取自訂的資料報表。
- 取得GA的API權限:
  - 在抓取GA資料之前，我們需要先有API的權限，google才能確保是妳本人，如何創建api我把方法放在下面。
  
<img src='https://i.imgur.com/apwSElu.jpg' height=500 weight =500>

- GA API版本
  - GA API版本目前正在運行的有兩種，v3跟v4，而在這邊我一開始找到的做法是v4，但隨後因為v3有的資料較多而更換了版本，在這邊也要給大家一個觀念，這裡講的或別人說版本是只抓取service的版本，而抓取real time和setting的版本目前都只有v3，後面會在補充。
- GA帳戶層級
  - GA帳戶層級分三個，帳戶、資源、資料檢視
  - 帳戶也就是AccountId，通常GA API金鑰帳戶會放在這邊帳戶使用者管理。
  - 資源也就是WebpropertyId，各公司可能會依照不同需求、地區等因素，新增不同的資源。
  - 資料檢視也就是ViewId，所有的資料都是歸屬於檢視層，公司可能會依照網站架構有不同需求而新增不同檢視。

<img src='https://i.imgur.com/QF5y0hw.jpg' height=250 weight =420>

- GA資料層級
  - GA資料層級可以分為三大項，使用者、工作階段、匹配
  - 使用者（User）：記錄個別的使用者，也就是這個「人」
  - 工作階段（Session）：紀錄單次造訪網頁與離開網頁的過程
  - 匹配（Hit）：紀錄所有使用者與網站之間的互動，包括頁面瀏覽、點擊按鈕、提交表單等等。

下面附上一張從知名的網路行銷公司awooo網站找到的一張範例圖

<img src='https://www.awoo.com.tw/wp-content/uploads/2018/10/japan-example-1024x536.png' height=300 weight =400>

- GA API資料抓取
  - GA API可以抓取得東西相當多，那我也只先介紹我工作上用到的三個
  
<img src='https://i.imgur.com/Pt8bD2T.jpg' height=300 weight =400>

  - core reporting api:基本上你在GA報表中看到的一般報表都是藉由這個API抓取的，比如熱門事件報表、網頁瀏覽量、跳出率等等。
  - real time reporting api:跟及時有關的數據就要透過這個API實現，比如現在此刻在我網站上的瀏覽人是有多少。
  - management api:任何跟帳戶有關的設定都可以從這邊抓取，比如有無開啟電子商務設定、有無目標設定、如何設定等等。
