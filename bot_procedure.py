import json
import requests
import time
from access_token import access_token

#finding correct group me group and getting those memebrs
def getNumMembers(data, group_name):
     for group in json_data["response"]:
        if (group["name"] == group_name):
            num_members = len(group["members"])
            return num_members

def getNewMemberInfo(data, group_name, num_new):
    name_list = []
    for group in json_data["response"]:
        if (group["name"] == group_name):
            num_members = len(group["members"])
            for x in range(1,num_new+1):
                name_list.append(group["members"][num_members - x]["name"])
            return name_list

def getJSONdata():
    #url for retrieving group ID's
    url = 'https://api.groupme.com/v3/groups?token='
    url += access_token

    #getting json data
    r = requests.get(url)
    json_data = r.json()
    return json_data

#detects new members being added and gives them welcome message + 
#other important info.
group_name = "Test Group"

while (True):
    json_data = getJSONdata()

    print("Update: " + str(time.time()))

    #checking for new members
    num_members = getNumMembers(json_data, group_name)
    print(num_members)
    time.sleep(5)

    json_data = getJSONdata()

    num_members_updated = getNumMembers(json_data, group_name)
    print(num_members_updated)

    #getting num of new members
    num_new_members = num_members_updated - num_members

    #if new members, print message to each of them
    if (num_new_members > 0):
        new_member_list = getNewMemberInfo(json_data, group_name,num_new_members)

        #initializing header and url
        url = 'https://api.groupme.com/v3/bots/post'

        headers = {
            'Content-Type': 'application/json',
        }
        #Greeting New Members
        for name in new_member_list:
            print("Welcoming " + str(name) + " to Group")
           
            greeting_message = "Hey " + str(name) + "! Welcome to the OpenMI GroupMe. For quicker updates, make sure to join our" \
                " mailing list: https://mcommunity.umich.edu/#group/members:OpenMi%20at%20Umich       Click here to join our LinkedIN" \
                " page: https://www.linkedin.com/groups/12578317/"

            message_data = {
                'bot_id': "6cce3106596c38b771da4fb5ee",
                'text': str(greeting_message),
            }

            response = requests.post(url, headers=headers, json=message_data)

            try:
                print("Message Error: Check data.json")
                with open('data.json', 'w', encoding='utf-8') as outfile:
                    json.dump(response.json(), outfile, ensure_ascii=False, indent=4)
            except:
                print("Message Printed Successfully")








