import tweepy
import json
from time import sleep
from credentials import *
from classes.tuit import Tuit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

data = api.search(q='AyudaCDMX',
        result_type="recent")
# print(data[1])

tuits = []

for d in data:
    tuits.append(Tuit(d.author.screen_name, d.text))


for t in tuits:
    print(t.toString())
