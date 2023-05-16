# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nitinsharma.atlassian.net/wiki/rest/api/content/163996?expand=body.storage"

auth = HTTPBasicAuth("nitinsh3101@gmail.com", "ATATT3xFfGF0L-1yIZJFsQRsOwpQc3t5FlxR-j0MCdnX1lI_QJfO9iTF1Tk2DhTGkYgJw1fwlZR-wB4-K9iKTpKfVw1JVQaXY0ILk9CGIZnTqOBzm_vn7645OF-2gX3TCAtLn5icWGXzTCrQEpIzECMpRzQ-BFkfPlseXKJ-HM57FlwsozzzmdA=277CCEC3")

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
