# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nitinsharma.atlassian.net/wiki/api/v2/pages/98389"

auth = HTTPBasicAuth("nitinsh3101@gmail.com", "ATATT3xFfGF0jcXtpXuFzIzwVgjz6kLaXOXUcnwnUrctjrJWPRneazitZ9XXk0sD4smXaGKyuTI0jia305oyn8Mn4oN3kXI-HAlfqyoNLDIBTb_vnGAJpIthuG-xp0EeBpkmDImw-hvp7c4Ln_wW1CQmGClChhk_wYFwG_EFl4pyFTBAuxQYjhI=95843A30")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "id": "98389",
  "status": "current",
  "title": "Overview",
  "spaceId": "98306",
  "body": {
    "representation": "storage",
    "value": "Hello, this is my first page."
  },
  "version": {
    "number": 2,
    "message": "update through api"
  }
} )

response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(response)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))