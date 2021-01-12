import tweepy 
import pandas as pd 


# API keys hidden on desktop
keyFile = open('C:\\Users\\walee\\Desktop\\access_key.txt', "r")
access_key = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\access_token.txt', "r")
access_token = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\secret_key.txt', "r")
secret_key = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\secret_token.txt', "r")
secret_token = keyFile.read()

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
df = pd.DataFrame(data=col1, index=[0])

df.to_csv("ElonMusk_Tweets.csv", index=False)