from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'go-url-1044-213d62415432.json' #API金鑰
VIEW_ID = '110032918' #Google Analytics 資料檢視層ID




# Reporting API初始化與授權

def initialize_analyticsreporting():
 
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics

analytics = initialize_analyticsreporting()

#抓資料
def get_report(analytics):
  
  
    return analytics.reports().batchGet(
        body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '2019-10-01', 'endDate': '2019-10-31'}],
                'metrics': [{'expression': 'ga:totalEvents'}],
                'dimensions': [{"name": "ga:pagePath"}],
                'orderBys': [{"fieldName": "ga:totalEvents", "sortOrder": "DESCENDING"}],
                "dimensionFilterClauses": [{
                   "filters": [{
                    "dimension_name": "ga:eventCategory",
                    "operator": "PARTIAL",
                    "expressions": ["Scroll Depth"]
                                }]
                                          }],
                'pageSize': 3
            }]
    }
  ).execute()

get_report(analytics)
# {'reports': [{'columnHeader': {'dimensions': ['ga:pagePath'],
#     'metricHeader': {'metricHeaderEntries': [{'name': 'ga:totalEvents',
#        'type': 'INTEGER'}]}},
#    'data': {'rows': [{'dimensions': ['/?p=3501'],
#       'metrics': [{'values': ['3138']}]},
#      {'dimensions': ['/'], 'metrics': [{'values': ['2253']}]},
#      {'dimensions': ['/?p=2149'], 'metrics': [{'values': ['2093']}]}],
#     'totals': [{'values': ['45357']}],
#     'rowCount': 689,
#     'minimums': [{'values': ['1']}],
#     'maximums': [{'values': ['3138']}],
#     'isDataGolden': True},
#    'nextPageToken': '3'}]}
# -----------------------------------------------------------------------------------------------------

res=get_report(analytics)
path=[]
for i in res['reports'][0]['data']['rows']:
    path.append(i['dimensions'][0])

def get_report(analytics):
    return analytics.reports().batchGet(
        body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '2019-10-01', 'endDate': '2019-10-31'}],
                'metrics': [{'expression': 'ga:pageviews'}],
                'dimensions': [{"name": "ga:pagePath"},{'name':"ga:sourceMedium"}],
                'orderBys': [{"fieldName": "ga:pageviews", "sortOrder": "DESCENDING"}],
                "dimensionFilterClauses": [{
                   "filters": [{
                    "dimension_name": "ga:pagePath",
                    "operator": "IN_LIST",
                    "expressions": path
                                }]
                                          }],
                #'pageSize': 3
            }]
    }
  ).execute()

print(path) # ['/?p=3501', '/', '/?p=2149']
print(get_report(analytics))
# {'reports': [{'columnHeader': {'dimensions': ['ga:pagePath',
#      'ga:sourceMedium'],
#     'metricHeader': {'metricHeaderEntries': [{'name': 'ga:pageviews',
#        'type': 'INTEGER'}]}},
#    'data': {'rows': [{'dimensions': ['/?p=3501', 'google / organic'],
#       'metrics': [{'values': ['1301']}]},
#      {'dimensions': ['/?p=2149', 'yahoo / organic'],
#       'metrics': [{'values': ['540']}]},
#        ...
#        ...
#        ...
#      {'dimensions': ['/?p=2149', 'opti-page.com / referral'],
#       'metrics': [{'values': ['1']}]},
#      {'dimensions': ['/?p=2149', 'search.avira.com / referral'],
#       'metrics': [{'values': ['1']}]}],
#     'totals': [{'values': ['4119']}],
#     'rowCount': 31,
#     'minimums': [{'values': ['1']}],
#     'maximums': [{'values': ['1301']}],
#     'isDataGolden': True}}]}
# -----------------------------------------------------------------------------------------------------

res=get_report(analytics)
import json
new_json = json.dumps(res)
def print_response(response):
    for report in response.get('reports', []): #將上述reports回應的內容取回並做為for迴圈基底
        columnHeader = report.get('columnHeader', {}) 
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
        dimensions = row.get('dimensions', [])
        dateRangeValues = row.get('metrics', [])

    for header, dimension in zip(dimensionHeaders, dimensions):
        cities.append(dimension)
        print (header + ': ' + dimension)
  
    for i, values in enumerate(dateRangeValues):
        
        for metricHeader, value in zip(metricHeaders, values.get('values')):
            val.append(int(value))
            print (metricHeader.get('name') + ': ' + value)   

print_response(res)
# ga:pagePath: /?p=2149
# ga:sourceMedium: search.avira.com / referral
# ga:pageviews: 1

print(res)
# {'reports': [{'columnHeader': {'dimensions': ['ga:country'],
#     'metricHeader': {'metricHeaderEntries': [{'name': 'ga:sessions',
#        'type': 'INTEGER'}]}},
#    'data': {'rows': [{'dimensions': ['Taiwan'],
#       'metrics': [{'values': ['8']}]}],
#     'totals': [{'values': ['8']}],
#     'rowCount': 1,
#     'minimums': [{'values': ['8']}],
#     'maximums': [{'values': ['8']}]}}]}

print(res.get('reports', []))
# [{'columnHeader': {'dimensions': ['ga:country'],
#    'metricHeader': {'metricHeaderEntries': [{'name': 'ga:sessions',
#       'type': 'INTEGER'}]}},
#   'data': {'rows': [{'dimensions': ['Taiwan'],
#      'metrics': [{'values': ['8']}]}],
#    'totals': [{'values': ['8']}],
#    'rowCount': 1,
#    'minimums': [{'values': ['8']}],
#    'maximums': [{'values': ['8']}]}}]

print(a.get('columnHeader', {}).get('metricHeader', {}).get('metricHeaderEntries', []))
# [{'name': 'ga:sessions', 'type': 'INTEGER'}]
