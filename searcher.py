import tweepy
import json
from time import sleep
from credentials import *
from keywords import *
from classes.tuit import Tuit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

data = api.search(q='@comoayudarmx',
        result_type="recent")

print("!!!!TODA DATA!!!!")
print(data[1])
print("!!!TODA DATA!!")
tuits = []



counter = 0

while counter < 1:
    data = api.search(q='@comoayudarmx',
            result_type="recent")

    for d in data:
        tuits.append(Tuit(d.author.screen_name, d.text, d.id_str))

    counter += 1

#for t in tuits:
 #   print(t.toString())


tuitsFiltrados = []

for t in tuits:
    for kw in kws:
        if t.getText().lower().find(kw) != -1 and t.getAuthor() != 'comoayudarmx' and t.getText().lower().find('comoayudarmx:') == -1:
            if len(t.getText().split()) > 4:
                tuitsFiltrados.append(t)
            

tuitsFiltrados = list(set(tuitsFiltrados))


for t in tuitsFiltrados:
    print(t.toString())

for t in tuitsFiltrados:
    try:
        api.retweet(t.getIdt())
    except:
        print("No new tweets")
        
