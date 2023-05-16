# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os
from requests.auth import HTTPBasicAuth
import json

url = "https://nitinsharma.atlassian.net/wiki/rest/api/content/163996?expand=body.storage"
confluence_api_token = os.environ.get('CONFLUENCE_API_TOKEN')

auth = HTTPBasicAuth("nitinsh3101@gmail.com", confluence_api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(response)
#temp=json.loads(response.text)
#print(temp['body']['storage']['value'])

#print()
#print(json.dumps(json.loads(response.content), sort_keys=True, indent=4, separators=(",", ": ")))
