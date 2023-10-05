import MySQLdb
from sqlalchemy import create_engine
import random
import pandas as pd

engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '', '127.0.0.1:3306', 'wellslu'))
con = engine.connect()#先連到資料庫

if __name__ == "__main__":
	df = pd.DataFrame({'a':[4,5],
	                  'b':['He','She']})#創建一個等等測試鑰丟到資料庫的df
	df.to_sql(name='test', con=con, if_exists='append', index=False)#在用append加進去已有的資料表中
	
	db = MySQLdb.connect("127.0.0.1", "root", "", "wellslu", charset='utf8' )#連到資料庫
	cursor = db.cursor()
	
	cursor.execute('''SELECT * FROM test''')#選取資料表，這邊用的是sql語法
	results = cursor.fetchall()#將結果取出
	
	for row in results:#print裡面的資料
	    print(row)
		# (1, 'I')
		# (2, 'You')
		# (3, 'We')
		# (4, 'He')
		# (5, 'She')
		# (4, 'He')
		# (5, 'She')
		# (4, 'He')
		# (5, 'She')
		# (4, 'He')
		# (5, 'She')
	
	db.close()#關閉db
