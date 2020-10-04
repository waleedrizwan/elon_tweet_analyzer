# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:31:59 2020

@author: walee
"""

#consumer_key =  'MdLc2PWvaUh4ZCQn0DJESoe4n'               
#consumer_secret = 'M7PqFUKvpV2MtnvvLRpo0mvg5ZDQgaa5JlavUxy5YgFlDONEeL'
#access_token_key ='AAAAAAAAAAAAAAAAAAAAAPZOIAEAAAAA%2FZ17URJXP8A70lafAvZseMwsShE%3DJTNVn6ltA37TaghBmtKyPmvhN9qIJwDFGrCeHgP0BLuRWoRuhf')




# requires authentation from Twittter Developer Community 


import tweepy 
import pandas as pd 

auth = tweepy.OAuthHandler('MdLc2PWvaUh4ZCQn0DJESoe4n', 'M7PqFUKvpV2MtnvvLRpo0mvg5ZDQgaa5JlavUxy5YgFlDONEeL')
auth.set_access_token('1309966965663035392-4YY7ERbSPWTFyPoAHwCQr0K7c0FtYC', 'RPBhXHjoumebhiURAQ7D5HZtq2EaBFwHsoZKQxn7bBiXo')

api = tweepy.API(auth)

tweetList = api.user_timeline(screen_name='elonmusk', tweet_mode="extended", count = 200)
actualTextList = []


for x in tweetList:
    print(x.full_text.replace("@", "").replace("RT", "")+ '\n')
    actualTextList.append(x.full_text.replace("@", "").replace("RT", ""))
 
    
'''   
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df
   col1  col2
0     1     3
1     2     4   
'''

  
col1 = {'tweet': actualTextList}
df = pd.DataFrame(data=col1)

## Next step remove non alphanumeric characters

## manually add labels to each tweet 
## train ML algo using the logic from the Udemy course 
    


    