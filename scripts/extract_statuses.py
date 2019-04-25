import tweepy
import pickle
from tqdm import tqdm
with open('archives/all_streaming_api5.obj', 'rb') as archive_file, \
        open('archives/asa5.txt', 'w') as plaintext_output:
    archive = pickle.load(archive_file)
    for key, value in tqdm(archive.items()):
        """
        We only want English tweets.
        We only want geotagged tweets or those with locations because we can't 
        do anything about them otherwise. 
        Fields: tweet ID, tweet timestamp, user ID, lat/long, tweet text
        """
        if value.lang != 'en':
            continue

        if (value.coordinates and not value.geo) or \
                (value.geo and not value.coordinates):
            import pdb; pdb.set_trace()

        if value.coordinates:
            tweet_id = value.id
            tweet_timestamp = value.created_at
            user_id = value.author.id
            tweet_coordinates = value.coordinates
            tweet_text = value.text
            plaintext_output.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(
                    tweet_id, tweet_timestamp, user_id,
                    (tweet_coordinates['coordinates'][0],
                    tweet_coordinates['coordinates'][1]),
                    tweet_text))

