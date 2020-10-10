# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:31:59 2020

@author: Waleed

Extracts the text from 200 most recent tweets
needed to train model 

"""



import tweepy 
import pandas as pd 


f = open('C:\\Users\\walee\\Desktop\\access_key.txt', "r")
access_key = f.read()

f = open('C:\\Users\\walee\\Desktop\\access_token.txt', "r")
access_token = f.read()

f = open('C:\\Users\\walee\\Desktop\\secret_key.txt', "r")
secret_key = f.read()

f = open('C:\\Users\\walee\\Desktop\\secret_token.txt', "r")
secret_token = f.read()

# requires authentation from Twittter Developer Community 
auth = tweepy.OAuthHandler(access_key, access_token)
auth.set_access_token(secret_key, secret_token)

api = tweepy.API(auth)

tweetList = api.user_timeline(screen_name='elonmusk', tweet_mode="extended", count = 200)

actualTextList = []

for x in tweetList:
    # remove any instances of @ and RT 
    text = x.full_text.replace("@", "").replace("RT", "")
    # removes non alphanumeric characters such as emojis
    for elm in text:
        if not(elm.isalnum()) and elm != " ":
            text = text.replace(elm, "")                 
    actualTextList.append(text)
            
    
# Creates series object containing 200 Tweets  
col1 = {'Tweets': actualTextList}
df = pd.DataFrame(data=col1)

df.to_csv("ElonMusk_Tweets.csv", index=False)


## manually add labels to each tweet 
## train ML algo using the logic from the Udemy course 
    


    