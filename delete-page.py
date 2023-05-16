# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth

url = "https://nitinsharma.atlassian.net/wiki/api/v2/pages/98389"

auth = HTTPBasicAuth("nitinsh3101@gmail.com", "ATATT3xFfGF0jcXtpXuFzIzwVgjz6kLaXOXUcnwnUrctjrJWPRneazitZ9XXk0sD4smXaGKyuTI0jia305oyn8Mn4oN3kXI-HAlfqyoNLDIBTb_vnGAJpIthuG-xp0EeBpkmDImw-hvp7c4Ln_wW1CQmGClChhk_wYFwG_EFl4pyFTBAuxQYjhI=95843A30")


response = requests.request(
   "DELETE",
   url,
   auth=auth
)

print(response)
print(response.text)