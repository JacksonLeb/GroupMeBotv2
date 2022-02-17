import json
import requests
from access_token import access_token

#url for retrieving group ID's
url = 'https://api.groupme.com/v3/groups?token='
url += access_token

#getting json data
r = requests.get(url)
json_data = r.json()

#ouptut json
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent=4)