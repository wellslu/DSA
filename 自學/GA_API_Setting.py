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
	    a=service.management().profiles().get(
	    accountId='68833467',
	    webPropertyId='UA-68833467-1',
	    profileId='110032918').execute()
	
	except TypeError as error:
	  # Handle errors in constructing a query.
	    print ('There was an error in constructing your query : %s' % error)
	
	except HttpError as error:
	  # Handle API errors.
	    print ('Arg, there was an API error : %s : %s' %
	        (error.resp.status, error._get_reason()))
	print(a)
	# {'id': '110032918',
	#  'kind': 'analytics#profile',
	#  'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/68833467/webproperties/UA-68833467-1/profiles/110032918',
	#  'accountId': '68833467',
	#  'webPropertyId': 'UA-68833467-1',
	#  'internalWebPropertyId': '105721505',
	#  'name': '所有網站資料',
	#  'currency': 'TWD',
	#  'timezone': 'Asia/Taipei',
	#  'websiteUrl': 'http://xingyetsai.com',
	#  'excludeQueryParameters': 'fbclid',
	#  'siteSearchQueryParameters': 's,tag',
	#  'stripSiteSearchQueryParameters': False,
	#  'type': 'WEB',
	#  'permissions': {'effective': ['READ_AND_ANALYZE']},
	#  'created': '2015-10-14T06:52:16.631Z',
	#  'updated': '2019-08-20T09:17:47.773Z',
	#  'eCommerceTracking': False,
	#  'botFilteringEnabled': True,
	#  'parentLink': {'type': 'analytics#webproperty',
	#   'href': 'https://www.googleapis.com/analytics/v3/management/accounts/68833467/webproperties/UA-68833467-1'},
	#  'childLink': {'type': 'analytics#goals',
	#   'href': 'https://www.googleapis.com/analytics/v3/management/accounts/68833467/webproperties/UA-68833467-1/profiles/110032918/goals'}}
