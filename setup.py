# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:38:31 2019

@author: edbras
"""

import json
import glob
from tweepy import OAuthHandler,API,Stream
from slistener import SListener


def load_cred():

    with open('twitter_credentials.json') as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']
    
    return consumer_key, consumer_secret, access_key, access_secret

consumer_key, consumer_secret, access_token, access_token_secret = load_cred()

#Authorization and initialization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth)

# Set up words to track
keywords_to_track = ['#Punisher']#,'#LukeCage', '#IronFist', '#Daredevil',

# Instantiate the SListener object 
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)

# Begin collecting data
stream.filter(track = keywords_to_track)
print (stream)


#Load JSONs
tweet_list = []

for file in glob.glob("streamer* - Copy.json"):
    with open(file, 'r') as tweet_data:
        tweets_json = filter(None,tweet_data.read().split("\n"))
    
    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)
        tweet_list.append(tweet_obj)
        
print(len(tweet_list))

#print(tweet['text'])
                     
                     
#Historical Tweets (API only allows 2 weeks)

"""
import csv
from tweepy import Cursor
csvFile = open('netflix.csv','w')

csvWriter = csv.writer(csvFile)

for tweet in Cursor(api.search, q = keywords_to_track, count=100,
                           lang = 'en', since = '2018-11-01').items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8')])
"""