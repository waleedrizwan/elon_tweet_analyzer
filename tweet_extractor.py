# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:31:59 2020

@author: walee
"""

#consumer_key =  'MdLc2PWvaUh4ZCQn0DJESoe4n'               
#consumer_secret = 'M7PqFUKvpV2MtnvvLRpo0mvg5ZDQgaa5JlavUxy5YgFlDONEeL'
#access_token_key ='AAAAAAAAAAAAAAAAAAAAAPZOIAEAAAAA%2FZ17URJXP8A70lafAvZseMwsShE%3DJTNVn6ltA37TaghBmtKyPmvhN9qIJwDFGrCeHgP0BLuRWoRuhf')


# requires authentation from Twittter Developer Community 
import twitter
import sys

api = twitter.Api(consumer_key='MdLc2PWvaUh4ZCQn0DJESoe4n',
                  consumer_secret='M7PqFUKvpV2MtnvvLRpo0mvg5ZDQgaa5JlavUxy5YgFlDONEeL',
                  access_token_key='1309966965663035392-4YY7ERbSPWTFyPoAHwCQr0K7c0FtYC',
                  access_token_secret='RPBhXHjoumebhiURAQ7D5HZtq2EaBFwHsoZKQxn7bBiXo')

user = 'elonmusk'
statuses = api.GetUserTimeline(screen_name=user)


# prints out recent tweets
tweets = [] 
for status in statuses:
    #print(status.text)
    tweets.append(status.text)
 
    
'''
# returns 100 most recent tweets when Twitter is searched on the application 
results = api.GetSearch(
    raw_query="q=Tesla%20&result_type=recent&since=2014-07-19&count=100000")

searchForTweets = []
for r in results:
    searchForTweets.append(r.text)
'''


    
    