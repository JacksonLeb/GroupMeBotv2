import json
import requests
from access_token import access_token

#parsing through General json info to get groupID
def findGroupID(group_name, json_info):
    for group in json_info["response"]:
        if (group["name"] == group_name):
            id = group["group_id"]
            return id

#url for retrieving group ID's
url = 'https://api.groupme.com/v3/groups?token='
url += access_token

#getting json data
r = requests.get(url)
json_data = r.json()

#groupID retrieval
group_name = "Test Group"
group_id = findGroupID(group_name, json_data)
print(group_id)

#registering bot
headers = {
    'Content-Type': 'application/json',
}
bot_data = {
    'bot': {
        'name': 'OpenMI Bot v2',
        'group_id': str(group_id),
    },
}

url = 'https://api.groupme.com/v3/bots?token='
url += access_token

print("Hello")
r = requests.post(url, headers=headers, json=bot_data)
print(r)

#ouptut json
with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent=4)







