# import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle

data = pd.read_csv("ElonMusk_Tweets.csv", encoding = "ISO-8859-1")


## Adjust to account for differences in csv files 

# extract the column which contains the Tweets
X = data.loc[0]

# tokenize the text from tweet and convert data in matrix format
vectorizer = CountVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)
print(X_vec) # Scipy sparse matrix
pickle.dump(vectorizer, open("vectorizer_elon_tweets", 'wb')) # Save vectorizer for reuse
X_vec = X_vec.todense() # convert sparse matrix into dense matrix

# Transform data by applying term frequency inverse document frequency (TF-IDF) 
tfidf = TfidfTransformer() #by default applies "l2" normalization
X_tfidf = tfidf.fit_transform(X_vec)
X_tfidf = X_tfidf.todense()

##Apply Naive Bayes algorithm to train data

# Extract the news body and labels for training the classifier
X_train = X_tfidf[:66,:]
Y_train = data.iloc[:66,2]


# Train the NB classifier
clf = GaussianNB().fit(X_train, Y_train) 
pickle.dump(clf, open("nb_elon_tweets", 'wb')) # Save classifier for reuse
