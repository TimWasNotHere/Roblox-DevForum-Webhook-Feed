# Roblox DevForum Update Feed via Webhooks
Get all updates from the Roblox DevForum update category via webhooks!

## Required:
- MongoDB Atlas (or you can use your own preferred DB)
- Webhook URL

## How to set up?
- Set up your MongoDB Atlas or your preferred DB
- In config.py:
   - add your connection string as uri
   - add your database name and the collection name in the destinations labaled database and connection
   - add your webhook url in the destination labeled webhookURL

After setting all the placeholder values, you can run it and it'll begin checking every five minutes for any new announcements. This can also be changed in config.py (cooldown)
