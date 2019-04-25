from location_stream_listener import LocationStreamListener
import tweepy
from secret import CONSUMER_KEY, CONSUMER_SECRET, \
        ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# TODO: Standard American, AAVE, Chicano, Southern Am, Appalachian
locations = {
    "singapore": [103.546519,1.195364,104.089498,1.470862],
    "india": [68.67,8.06,79.62,23.86,
        70.84,23.86,79.62,34.44,
        79.51,15.27,88.3,26.58],
    "uk": [-10.67,50.25,1.53,61.07],
    "canada-french": [-74.0846,45.4259,-70.5037,47.3132],
    "australia": [112.4,-43.74,155.64,-10.95],
    "new_zealand": [165.55,-47.94,178.91,-33.1]
}

bounding_boxes = []
for box in locations.values():
    bounding_boxes += box
print(bounding_boxes)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

stream_listener = LocationStreamListener('../stream_output/output')
stream = tweepy.Stream(auth = api.auth, listener=stream_listener)

stream.filter(locations=bounding_boxes,
                is_async=True)
