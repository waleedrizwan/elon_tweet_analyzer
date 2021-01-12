import pickle
import pandas as pd
import tweepy
import time
from sklearn.feature_extraction.text import TfidfTransformer
import requests
import smtplib


# API keys hidden in textfiles
keyFile = open('C:\\Users\\walee\\Desktop\\access_key.txt', "r")
access_key = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\access_token.txt', "r")
access_token = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\secret_key.txt', "r")
secret_key = keyFile.read()

keyFile = open('C:\\Users\\walee\\Desktop\\secret_token.txt', "r")
secret_token = keyFile.read()

cumulative_tweets = []

def newTweet():
    '''
    checks to see if a new tweet not contained
    in historic_tweets has been made
    if new tweet adds to cumulative_tweets
    and return True, false otherwise
    :param: None
    :return: Bool
    '''

    # uses AuthHandler authentation from Twittter Developer Community 
    auth = tweepy.OAuthHandler(access_key, access_token)
    auth.set_access_token(secret_key, secret_token)

    api = tweepy.API(auth)

    # user_timeline method retrives most recent tweet made by user
    newestTweet = api.user_timeline(screen_name='elonmusk', tweet_mode="extended", count = 1)[0] # status object
    
    # full_text method called to return tweet string from status object    
    # remove any instances of @ and RT 
    newestTweet = newestTweet.full_text.replace("@", "").replace("RT", "")
    # removes non alphanumeric characters such as emojis
    for elm in newestTweet:
        if not(elm.isalnum()) and elm != " ":
            newestTweet = newestTweet.replace(elm, "")  

    # if the newest tweet is not in the historic tweet log a new tweet must be analyzed
    if not(newestTweet in cumulative_tweets):
        cumulative_tweets.append(newestTweet)
        return True
    else:
        return False


def sendEmail(signal):
    
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Establishes connection to GMAIL Server, host data is parameter
    server.ehlo()  # Server identifies itself to Host Server
    server.starttls()  # Encrypts Connection

    # Login to google server with  GMAIL Information
    server.login("w2rizwan@gmail.com", "")

    if signal == "Pos":
        decision = "Recent Tweet has been predicted to increase the price of TSLA in the short term"
    else:
        decision = "Recent Tweet has been predicted to decrease the price of TSLA in the short term"


    # Email subject
    subject = "Tweet Analysis"
    # Body paragraph of email
    body = decision
    # Stores subject and body inside msg
    msg = f"Subject:{subject}\n\n{body}"

    # Sends "msg" to recipient
    server.sendmail(
        'w2rizwan@gmail.com',  # From
        'w2rizwan@uwaterloo.ca',  # To
        msg
    )
    print("Hey Email Has been Sent")  # Confirms Email has been sent
    server.quit() # Closes Connection to Google Server


def analyzeTweet():
    '''
    Performs sentiment anaylsis on newest
    tweet made by Elon
    if an impact on TSLA is predicted
    calls sendEmail
    :param: 
    :return: None
    '''

    newTweetList = cumulative_tweets[0]
    
    # prints newest tweet to excel sheet so model can understand
    col1 = {'Tweets': newTweetList}
    df = pd.DataFrame(data=col1, index=[0])
    df.to_csv("Sentiment_Analysis_File.csv", index=False)

    #Importing trained classifier and fitted vectorizer
    nb_clf = pickle.load(open("nb_elon_tweets", 'rb'))
    vectorizer = pickle.load(open("vectorizer_elon_tweets", 'rb'))

    #Predict sentiment using the trained classifier

    # Import CSV containing newest Tweet
    data_pred = pd.read_csv("Sentiment_Analysis_File.csv", encoding = "ISO-8859-1")
    X_test = data_pred.iloc[:,0] # extract column with tweet 
    X_vec_test = vectorizer.transform(X_test) #don't use fit_transform here because the model is already fitted
    X_vec_test = X_vec_test.todense() #convert sparse matrix to dense

    # Transform data by applying term frequency inverse document frequency (TF-IDF) 
    tfidf = TfidfTransformer() #by default applies "l2" normalization
    X_tfidf_test = tfidf.fit_transform(X_vec_test)
    X_tfidf_test = X_tfidf_test.todense()

    # Predict the sentiment values
    y_pred = nb_clf.predict(X_tfidf_test)

    sentiment = y_pred[0]    
    
    if sentiment == "Pos":
        print("Buy Signal Triggered")
        sendEmail("Buy")
    elif sentiment == "Neg":
        print("Sell Signal Triggered")
        sendEmail("Sell")
    else:
        print("Tweet predicted to have no impact")


# holds current time 
starttime = time.time()

# checks if a new tweet has been made every minute
while True:   
    print("Checking for new Tweet")
    
    if newTweet():
        print("Conducting Sentiment Analysis")
        # calls analyze tweet if a new tweet has been made
        analyzeTweet()
        print("Analysis Finished") 

    else:
        print("No new Tweets")             
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))





    

