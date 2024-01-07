#from functions.database import
from funct.devforum import getannouncement, getauthorpfp
from funct.misc import sendAnnouncement, checkID, saveLastID
import asyncio
from config import cooldown

print('starting...')

async def main():
    print("--------")
    while True:
        print("Checking DevForum")
        title, author, link, datePublished, summary, announcementID = getannouncement()
        check = checkID(announcementID)
        if check is False: # this means the announcement has not been announced before
            print("New announcement detected")
            save = saveLastID(announcementID)
            if save is True: # this means that the announcementID has been saved and will now send the announcement
                authorPFP_link = getauthorpfp(author)
                sendAnnouncement(title, author, link, datePublished, summary, authorPFP_link)
            else:
                print("There was an error saving the announcementID")
                break
        elif check is True:
            print("This was already announced.")
        else:
            print("There was an error.")
        await asyncio.sleep(cooldown)

asyncio.run(main())