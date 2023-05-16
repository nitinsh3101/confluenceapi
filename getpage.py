# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nitinsharma.atlassian.net/wiki/rest/api/content/163996?expand=body.storage"

auth = HTTPBasicAuth("nitinsh3101@gmail.com", "ATATT3xFfGF0jcXtpXuFzIzwVgjz6kLaXOXUcnwnUrctjrJWPRneazitZ9XXk0sD4smXaGKyuTI0jia305oyn8Mn4oN3kXI-HAlfqyoNLDIBTb_vnGAJpIthuG-xp0EeBpkmDImw-hvp7c4Ln_wW1CQmGClChhk_wYFwG_EFl4pyFTBAuxQYjhI=95843A30")

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
