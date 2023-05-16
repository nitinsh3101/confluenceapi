# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nitinsharma.atlassian.net/wiki/rest/api/content/163996?expand=body.storage"

auth = HTTPBasicAuth("nitinsh3101@gmail.com", "ATATT3xFfGF0rd0SEut20SrFRKeFij1dVihd6MVGbvKdKO797ChUkHmmsuolxPci6RmdPeeU1jvMJzVYXUkOxd4E6ilddauq9_MUp1j4oG1Q_CdPUYOyWYrQV-uDbLn6RUaQq3PflJ0OvoUmn-l8XaugkroGvqquPT2LJJ_6H6ugtx-jCA5Xxfo=DBF64C65")

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
