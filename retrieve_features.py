import re
import csv
train_tweets = 'train_tweets.txt'
test_tweets = 'test_tweets_unlabeled.txt'
tweets = []
authors = []
data_frame = {}


with open(train_tweets) as f:
    line = f.readline()
    while line:
        author = line.split('\t')[0]
        line = line.strip()

        if author not in authors:
            authors.append(author)
        tweet = line.split('\t')[1]
        tweet = tweet.lower()
        tweet = re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', tweet)
        # tweet = re.sub(r'@(\w+)', '', tweet)
        # tweet = re.sub(r'#(\w+)', '', tweet)
        if author in data_frame.keys():
            # print(author)
            data_frame[author]['word_count'] += len(tweet.split())
            data_frame[author]['character_count'] += len(tweet)
            data_frame[author]['tweet_count'] += 1
            data_frame[author]['digit_count'] += sum(c.isdigit() for c in tweet)
            data_frame[author]['colon_count'] += sum(c == ':' for c in tweet)
            data_frame[author]['semicolon_count'] += sum(c == ';' for c in tweet)
            data_frame[author]['qmark_count'] += sum(c == '?' for c in tweet)
            data_frame[author]['period_count'] += sum(c == ',' for c in tweet)
            data_frame[author]['comma_count'] += sum(c == '.' for c in tweet)
            data_frame[author]['exclamation_count'] += sum(c == '!' for c in tweet)
            data_frame[author]['@_count'] += sum(c == '@' for c in tweet)
            data_frame[author]['#_count'] += sum(c == '#' for c in tweet)
        else:
            # print(author)
            data_frame[author] = {}
            data_frame[author]['word_count'] = len(tweet.split())
            data_frame[author]['character_count'] = len(tweet)
            data_frame[author]['tweet_count'] = 1
            data_frame[author]['digit_count'] = sum(c.isdigit() for c in tweet)
            data_frame[author]['colon_count'] = sum(c == ':' for c in tweet)
            data_frame[author]['semicolon_count'] = sum(c == ';' for c in tweet)
            data_frame[author]['qmark_count'] = sum(c == '?' for c in tweet)
            data_frame[author]['period_count'] = sum(c == ',' for c in tweet)
            data_frame[author]['comma_count'] = sum(c == '.' for c in tweet)
            data_frame[author]['exclamation_count'] = sum(c == '!' for c in tweet)
            data_frame[author]['@_count'] = sum(c == '@' for c in tweet)
            data_frame[author]['#_count'] = sum(c == '#' for c in tweet)

        # print(data_frame)
        line = f.readline()
    f.close()

# # print(data_frame)
for key in data_frame:
    data_frame[key]['avg_word'] = data_frame[key]['word_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_character'] = data_frame[key]['character_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_digit'] = data_frame[key]['digit_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_colon'] = data_frame[key]['colon_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_semicolon'] = data_frame[key]['semicolon_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_qmark'] = data_frame[key]['qmark_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_period'] = data_frame[key]['period_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_comma'] = data_frame[key]['comma_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_exclamation'] = data_frame[key]['exclamation_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_@'] = data_frame[key]['@_count'] / data_frame[key]['tweet_count']
    data_frame[key]['avg_#'] = data_frame[key]['#_count'] / data_frame[key]['tweet_count']
csv_data = []

for key in data_frame:
    row = {'author': key, 'word': data_frame[key]['avg_word'], 'character': data_frame[key]['avg_character'],
           'digit': data_frame[key]['avg_digit'],
           'colon': data_frame[key]['avg_colon'], 'semicolon': data_frame[key]['avg_semicolon'],
           'qmark': data_frame[key]['avg_qmark'], 'period': data_frame[key]['avg_period'],
           'comma': data_frame[key]['avg_comma'], 'exclamation': data_frame[key]['avg_exclamation'],
           '@': data_frame[key]['avg_@'], '#': data_frame[key]['avg_#']}
    csv_data.append(row)

train_columns = ['author', 'word', 'character', 'digit', 'colon', 'semicolon', 'qmark', 'period', 'comma', 'exclamation',
                 '@', '#']
csv_columns = ['author', 'word_count', 'character_count', 'digit_count', 'colon_count', 'semicolon_count', 'qmark_count',
               'period_count', 'comma_count', 'exclamation_count', '@_count', '#_count']
test_columns = ['word', 'character', 'digit', 'colon', 'semicolon', 'qmark',
                'period', 'comma', 'exclamation', '@', '#']

try:
    with open('dataframe.csv', 'wb') as file:
        writer = csv.DictWriter(file, fieldnames=train_columns)
        writer.writeheader()

        for row in csv_data:
            writer.writerow(row)
except IOError as (errno, strerror):
    print('I/O error({0}): {1}'.format(errno, strerror))
#
# df = []
# with open(train_tweets) as f:
#     line = f.readline()
#     while line:
#         author = line.split('\t')[0]
#         line = line.strip()
#         if author not in authors:
#             authors.append(author)
#         tweet = line.split('\t')[1]
#         tweet = tweet.lower()
#         tweet = re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', tweet)
#         row = {'author': author, 'word_count': len(tweet.split()), 'character_count': len(tweet),
#                 'digit_count': sum(c.isdigit() for c in tweet), 'colon_count': sum(c == ':' for c in tweet),
#                 'semicolon_count': sum(c == ';' for c in tweet), 'qmark_count': sum(c == '?' for c in tweet),
#                 'period_count': sum(c == ',' for c in tweet), 'comma_count': sum(c == '.' for c in tweet),
#                 'exclamation_count': sum(c == '!' for c in tweet), '@_count': sum(c == '@' for c in tweet),
#                 '#_count': sum(c == '#' for c in tweet)}
#         df.append(row)
#         line = f.readline()
#     f.close()
#
#
# try:
#     with open('dataframe.csv', 'wb') as file:
#         writer = csv.DictWriter(file, fieldnames=csv_columns)
#         writer.writeheader()
#         for row in df:
#             writer.writerow(row)
# except IOError as (errno, strerror):
#     print('I/O error({0}): {1}'.format(errno, strerror))


test_data = []
with open(test_tweets) as f:
    line = f.readline()
    while line:
        line = line.strip()
        tweet = line.lower()
        tweet = re.sub(r'(http|https|ftp)://[a-zA-Z0-9\\./]+', '', tweet)
        row = { 'word': len(tweet.split()), 'character': len(tweet),
                'digit': sum(c.isdigit() for c in tweet), 'colon': sum(c == ':' for c in tweet),
                'semicolon': sum(c == ';' for c in tweet), 'qmark': sum(c == '?' for c in tweet),
                'period': sum(c == ',' for c in tweet), 'comma': sum(c == '.' for c in tweet),
                'exclamation': sum(c == '!' for c in tweet), '@': sum(c == '@' for c in tweet),
                '#': sum(c == '#' for c in tweet)}
        test_data.append(row)
        line = f.readline()
    f.close()

try:
    with open('test_data.csv', 'wb') as f:
        writer = csv.DictWriter(f, fieldnames=test_columns)
        writer.writeheader()
        for row in test_data:
            writer.writerow(row)
except IOError as (errno, strerror):
    print('I/O error({0}): {1}'.format(errno, strerror))
