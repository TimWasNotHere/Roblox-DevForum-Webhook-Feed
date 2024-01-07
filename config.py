from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "placeholder" # replace with your mongoDB connection string

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

client = MongoClient(uri, server_api=ServerApi('1'))

try:
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
  print(e)

database = client["placeholder"] # replace with your database's name
collection = database["placeholder"] # replace with your collection's name

webhookURL = "placeholder" # replace with your webhook URL

# this is how long it'll wait to recheck for any new announcements; its in seconds
cooldown = 300 # 300 seconds = 5 minutes