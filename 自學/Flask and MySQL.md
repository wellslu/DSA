# Flask
- Flask 是一個使用 Python 撰寫的輕量級 Web 應用程式框架，由於其輕量特性，也稱為 micro-framework（微框架）。Flask 核心十分簡單，主要是由 Werkzeug WSGI 工具箱和 Jinja2 模板引擎所組成，Flask 和 Django 不同的地方在於 Flask 給予開發者非常大的彈性（當然你也可以說是需要思考更多事情），可以選用不同的用的 extension 來增加其功能。相比之下，Django 雖然完善但技術選擇相對不彈性，不論是 ORM、表單驗證或是模版引擎都有自己的作法。事實上沒有最好的框架，只有合適的使用情境，Django 相比之下適合需要快速的開發大型的應用程式，和 Ruby 中的 Ruby on Rails 相似，而 Flask 則是相對輕量彈性，更像是 Ruby 界的 Sinatra。若讀者想先體驗看看 Flask 的程式狀況，以下是 Flask 簡易運行的程式，啟動測試伺服器後，可以在瀏覽器中（http://localhost:5000/）看到運行結果。
- 在使用flask之前記得先pip flask的套件。
參考網址:https://blog.techbridge.cc/2017/06/03/python-web-flask101-tutorial-introduction-and-environment-setup/ https://www.maxlist.xyz/2019/03/17/flask-get-post/ 

# Python 連結 MySQL
- 相信大家對MySQL都有一定程度的了解，這邊就不多作介紹了。
- 抓資料:抓資料的部份我這邊是透過MySQLdb連接，他相當早就有的一個連接模組，其內部核心是以 C 語言開發的。
- 修改資料:修改資料部份我是用SQLAlchemy，不是我不用MySQLdb，而是上網查聽說在python某一次改版就把MySQLdb地修改功能拿掉了，但上網查SQLAlchemy可以發現，相當多文章都是講用這個連接模組做flask，可能主要是因為他採用簡單的Python語言，為高效和高效能的資料庫存取設計，實現了完整的企業級持久模型。
參考資料:https://blog.gtwang.org/programming/python-mysqldb-connect-mysql-database-tutorial/ https://zh.wikipedia.org/wiki/SQLAlchemy https://blog.techbridge.cc/2017/08/12/python-web-flask101-tutorial-sqlalchemy-orm-database-models/
