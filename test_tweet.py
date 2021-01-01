import tweepy
from authentication import process_yaml, app_key, app_secret, oauth_token, oauth_token_secret

data =  process_yaml()
CONSUMER_KEY = app_key(data)
CONSUMER_SECRET = app_secret(data) 
ACCESS_KEY = oauth_token(data)  
ACCESS_SECRET = oauth_token_secret(data)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status('I am Herzl Bot.')