import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
train_tweets = "train_tweets.txt"
tweets = []
authors = []

def import_tweets(filename):
    with open(filename) as f:
        line = f.readline()
        while line:
            line = line.strip()
            author = line.split('\t')[0]
            authors.append(author)
            tweet = line.split('\t')[1]
            tweet = tweet.lower()
            # remove @handle
            tweet = re.sub(r'@(\w+)', '', tweet)
            # for word in tweet.split():
            #     if word in stopwords.words('english'):
            #         tweet = tweet.replace(word, '')
            # tweet = tweet.strip()
            # tweet = re.sub(' +', ' ', tweet)
            # remove punctuation (link will turn to word only, like httpwwwgooglecom
            tweet = re.sub(r'[^A-Za-z #\'-]+', '', tweet)
            # remove stopwords
            # tweet = [w for w in tweet.split() if w not in stopwords.words('english')]

            tweets.append(tweet)
            print(tweet)
            line = f.readline()
        f.close()


import_tweets(train_tweets)
vectorizer = TfidfVectorizer(stop_words='english', min_df=5, max_df=0.6, sublinear_tf=True, use_idf=True)
X = vectorizer.fit_transform(tweets)
features = []
features = vectorizer.get_feature_names()
print(vectorizer.get_feature_names())
print(X.shape)


X_train, X_test, y_train, y_test = train_test_split(X, authors, test_size=0.2, random_state=1337)

svm = LinearSVC()
svm.fit(X_train, y_train)

predictions = svm.predict(X_test)
print(list(predictions[0:10]))
print(y_test[:10])
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))

