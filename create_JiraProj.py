# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://rudragadekar1311.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF06zG4g225tPXXq29aSSL2tbnEp0Jfn91gJl0VX5QAkcNgOyCihMPzuvJHkKnNeZLEstUcuPrkC7JiiFIP7lH6ZaxJWzD6b1ih41K4qAy48ykcJskO9noWBSkW-uOWllwoIjhZAcKSm8KObaUrjdQbwpJ83haW2jyYdTV0r0nw7I8=8A8E5C09"

auth = HTTPBasicAuth("rudragadekar13@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira issue",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    "issuetype": {
      "id": "10014"
    },
    
    "project": {
      "key": "RD"
    },
    "summary": "First Jira ticket",
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
