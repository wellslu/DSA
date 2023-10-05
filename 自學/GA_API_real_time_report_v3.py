from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'go-url-1044-213d62415432.json' #API金鑰
VIEW_ID = '110032918' #Google Analytics 資料檢視層ID

def get_service():
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    service = build('analytics', 'v3', credentials=credentials)

    return service

if __name__ == "__main__":
	service = get_service()
	try:
	    a=service.data().realtime().get(
	    ids='ga:' + VIEW_ID,
	    metrics='rt:activeUsers',
	    dimensions='rt:medium').execute()
	
	except TypeError as error:
	  # Handle errors in constructing a query.
	    print ('There was an error in constructing your query : %s' % error)
	
	except HttpError as error:
	  # Handle API errors.
	    print ('Arg, there was an API error : %s : %s' %
	        (error.resp.status, error._get_reason()))

	print(a)
	# {'kind': 'analytics#realtimeData',
	#  'id': 'https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:110032918&dimensions=rt:medium&metrics=rt:activeUsers',
	#  'query': {'ids': 'ga:110032918',
	#   'dimensions': 'rt:medium',
	#   'metrics': ['rt:activeUsers'],
	#   'max-results': 1000},
	#  'totalResults': 2,
	#  'selfLink': 'https://www.googleapis.com/analytics/v3/data/realtime?ids=ga:110032918&dimensions=rt:medium&metrics=rt:activeUsers',
	#  'profileInfo': {'profileId': '110032918',
	#   'accountId': '68833467',
	#   'webPropertyId': 'UA-68833467-1',
	#   'internalWebPropertyId': '105721505',
	#   'profileName': '所有網站資料',
	#   'tableId': 'realtime:110032918'},
	#  'columnHeaders': [{'name': 'rt:medium',
	#    'columnType': 'DIMENSION',
	#    'dataType': 'STRING'},
	#   {'name': 'rt:activeUsers', 'columnType': 'METRIC', 'dataType': 'INTEGER'}],
	#  'totalsForAllResults': {'rt:activeUsers': '4'},
	#  'rows': [['(none)', '1'], ['ORGANIC', '3']]}
