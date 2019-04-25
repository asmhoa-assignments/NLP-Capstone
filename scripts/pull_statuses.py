import tweepy
from secret import CONSUMER_KEY, CONSUMER_SECRET, \
        ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweet_list = 'all_streaming_api.txt'
tweets = {}

archive_size = 5000
archive_index = 0

from tqdm import tqdm
import pickle

with open(tweet_list) as in_file:
    for line in tqdm(in_file):
        tweet_id = line.strip()
        try:
            tweet = api.get_status(tweet_id)
            tweets[tweet_id] = tweet
        except KeyboardInterrupt:
            exit(0)
        except:
            continue
        
        if len(tweets.keys()) == archive_size:
            with open('archives/all_streaming_api{0}.obj'.format(archive_index), 'wb') \
                    as out_file:
                pickle.dump(tweets, out_file)
            archive_index += 1
            tweets = {}

if len(tweets.keys()) > 0:
    with open('archives/all_streaming_api{0}.obj'.format(archive_index), 'wb') \
            as out_file:
        pickle.dump(tweets, out_file)

