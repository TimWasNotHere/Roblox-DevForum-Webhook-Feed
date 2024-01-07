import requests
import json
from config import webhookURL
from config import collection


# webhook stuff
def sendAnnouncement(title, author, link, datePublished, summary, authorPFP_link): # this will send the devforum announcement via the webook
    url = webhookURL
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
    "embeds": [
        {
        "title": f"[{title}]({link})",
        "description": summary,
        "footer": {
            "text": f"{author} | {datePublished}",
            "icon_url": authorPFP_link
        },
        }
    ]
    })
    requests.post(url, headers=headers, data=payload)


# DB stuff to ensure that the same update isnt sent twice
def saveLastID(announcementID):
    try:
        data = {"_id":str(announcementID)}
        collection.insert_one(data)
        return True # it worked
    except:
       return False # there was an error

def checkID(announcementID):
    print("Checking if its been announced before \nID:"+announcementID)
    DB = collection.find()
    for IDs in collection.find():
        ID = IDs['_id']
        if ID == announcementID:
            return True # this means this announcement has already been sent before
        else:
            return False # this means it has not been sent before
    return False # this usually will mean the DB is empty and ready for new announcement IDs