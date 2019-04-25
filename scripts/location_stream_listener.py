import tweepy
import sys
class LocationStreamListener(tweepy.StreamListener):
    def __init__(self, base_file, start_index=0):
        super(LocationStreamListener, self).__init__()
        self._index = start_index
        self._base_file = base_file
        self._tweets_written = 0

    
    def on_status(self, status):
        if status.place:
            tweet_id = status.id
            tweet_timestamp = status.created_at
            user_id = status.author.id
            tweet_city = status.place.full_name
            tweet_country = status.place.country
            tweet_text = status.text
            with open(f'{self._base_file}{self._index}', 'a') as output:
                try:
                    output.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\n'.format(
                        tweet_id, tweet_timestamp, user_id,
                        tweet_city, tweet_country,
                        (status.lang == 'en'),
                        tweet_text, 
                        (status.geo['coordinates'] if status.geo else '')))
                except:
                    e = sys.exc_info()
                    print(e)

            self._tweets_written += 1
            if self._tweets_written % 1000 == 0:
                print(self._tweets_written)
            # print(self._tweets_written)
            # if self._tweets_written == 5000:
            #     print('refresh')
            #     self._index += 1
            #     self._tweets_written = 0

    def on_error(self, status_code):
        if status_code == 420:
            print("Rate limited.  Exiting...")
            return False

