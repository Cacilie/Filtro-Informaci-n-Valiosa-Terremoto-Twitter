 # -*- coding: utf-8 -*-

import tweepy
import json
from time import sleep
from credentials import *
from keywords import *
from classes.tuit import Tuit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tuits = []

data = api.search(q='sismo', result_type="recent")

print "%s tuits encontrados" % (len(data))

for d in data:
    tuits.append(Tuit(d.author.screen_name, d.text, d.id_str))

tuitsFiltrados = []

for t in tuits:
    for kw in kws:
        if kw in t.getText().lower() and t.getAuthor() != 'comoayudarmx' and not 'comoayudarmx:' in t.getText().lower():
            if len(t.getText().split()) > 4:
                tuitsFiltrados.append(t)
            

tuitsFiltrados = list(set(tuitsFiltrados))

for t in tuitsFiltrados:
    print(t.toString())

print "%s tuits filtrados" % (len(tuitsFiltrados))

for t in tuitsFiltrados:
    try:
        api.retweet(t.getIdt())
    except:
        print("No new tweets")
        
