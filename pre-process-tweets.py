import re
from nltk.corpus import stopwords
train_tweets = "train_tweets.txt"
tweets = []


def import_tweets(filename):
    with open(filename, encoding='UTF8') as f:
        line = f.readline()
        while line:
            line = line.strip()
            tweet = line.split('\t')[1]
            tweet = tweet.lower()
            # remove @handle
            tweet = re.sub(r'@(\w+)', '', tweet)
            # remove punctuation (link will turn to word only, like httpwwwgooglecom
            tweet = re.sub(r'[^A-Za-z \d#\'-]+', '', tweet)
            # remove stopwords
            tweet = [w for w in tweet.split() if w not in stopwords.words('english')]
            tweets.append(tweet)
            # print(tweet)
            line = f.readline()
        f.close()


import_tweets(train_tweets)
