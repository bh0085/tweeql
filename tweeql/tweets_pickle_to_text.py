import sys
import pickle

#goes thru pickle file, writes to text all tweets in english

pickle_file = 'data/tweets.pickle'
out_file = './test_tweets.txt'

data = pickle.load(open(pickle_file,'rb'))
tweets_by_place = data['posts']
f = open(out_file,'w')

for place_tweet in tweets_by_place:
    for tweet_obj in place_tweet:
        if tweet_obj.iso_language_code == 'en':
            print tweet_obj.text
            try:
                f.write(tweet_obj.text)
                f.write('\n')
            except UnicodeEncodeError:
                print 'COULD NOT WRITE!\n'
