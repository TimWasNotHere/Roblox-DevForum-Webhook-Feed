import feedparser
from bs4 import BeautifulSoup
import requests
import os

def parse_html(html): # this formats the description to a more readable state
    elem = BeautifulSoup(html, features="html.parser")
    text = ""
    for e in elem.descendants:
        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br',  'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th']:
            text += '\n'
        elif e.name == 'li':
            text += '\n-'
    summary = os.linesep.join([s for s in text.splitlines() if s])
    return summary

def getannouncement():
    # gets the latest announcement from devforum
    devforumAnnouncements = feedparser.parse('https://devforum.roblox.com/c/updates/45.rss') # devforum link (this will get all updates from the update category)
    recentAnnouncement = devforumAnnouncements.entries[0]

    # announcement data
    title = recentAnnouncement.title # the title of the announcement
    author = recentAnnouncement.author # the poster
    link = recentAnnouncement.link # url to announcement
    datePublished = recentAnnouncement.published # date it was published
    announcementID = recentAnnouncement.id # the announcement's ID

    # this gets a summary of the announcement; first 400 characters of it
    summaryData = recentAnnouncement.description
    summary = f"{parse_html(summaryData)[:400]}..."

    return title, author, link, datePublished, summary, announcementID


def getauthorpfp(author):
    # to get the author's pfp
    authorProfileData = requests.get(f"https://devforum.roblox.com/u/{author}.json") # devforum author data

    authorAvatar_ID = authorProfileData.json()['user']['uploaded_avatar_id'] # the pfp ID

    authorPFP_link= f"https://doy2mn9upadnk.cloudfront.net/user_avatar/devforum.roblox.com/{author}/120/{authorAvatar_ID}_2.png" # the pfp url
    
    return authorPFP_link