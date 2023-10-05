import flask
from flask import Flask, request

#這邊我是用flask獲取我要的ga資訊後，再去ga挖資料
KEY_FILE_LOCATION = '' 
VIEW_ID = ''
ACCOUNTID = ''
WEBPROPERTYID = ''
item = ''

app = Flask(__name__)

@app.route('/test')
def index():
    global item,KEY_FILE_LOCATION,VIEW_ID,ACCOUNTID,WEBPROPERTYID
    KEY_FILE_LOCATION = request.args['json']
    item = request.args.get('itemid')
    VIEW_ID = request.args['viewid']
    ACCOUNTID = request.args['accountid']
    WEBPROPERTYID = request.args['webpropertyid']
    return KEY_FILE_LOCATION+' '+VIEW_ID+' '+ACCOUNTID+' '+WEBPROPERTYID+' '+item
	
if __name__ == '__main__':
        app.run(debug=False)
