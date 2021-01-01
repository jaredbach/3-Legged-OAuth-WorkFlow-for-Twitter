# 3-Legged OAuth Flow
# OAuth 1.0a
    # If you are wanting to make a request on behalf of a different Twitter account, that account’s owner must grant access to you by signing in to their account as part of the 3-legged OAuth flow. The output of this process is a set of access tokens (oauth_token and oauth_token_secret) that can be used to make a OAuth 1.0a request.



######################################################
############# Step 1: Defining Functions #############
######################################################

# Read secrets from YAML file
import yaml

# Open the file function
def process_yaml():
    with open('config.yaml') as file:
        return yaml.safe_load(file)

# Access API/app/consumer key function
def app_key(data):
    return data["twitter_api"]["app_key"]

# Access API/app/consumer secret function
def app_secret(data):
    return data["twitter_api"]["app_secret"]

# Access oauth_token function
def oauth_token(data):
    return data["twitter_api"]["oauth_token"]

# Access oauth_token_secret function
def oauth_token_secret(data):
    return data["twitter_api"]["oauth_token_secret"]



######################################################
###### Step 2: Initiate Authentication Process #######
######################################################

# Import requests
import requests

# Credentials from the application page
data =  process_yaml()
key = app_key(data)
secret = app_secret(data)

# OAuth URLs given on the application page
request_token_url = 'https://api.twitter.com/oauth/request_token'
authorization_url = 'https://api.twitter.com/oauth/authorize'
access_token_url = 'https://api.twitter.com/oauth/access_token'

# Fetch a request token
from requests_oauthlib import OAuth1Session
twitter = OAuth1Session(key, client_secret=secret, callback_uri='https://twitter.com')
twitter.fetch_request_token(request_token_url)

# Link user to authorization page
authorization_url = twitter.authorization_url(authorization_url)
print('Please go here and authorize,', authorization_url)

# Get the verifier code from the URL
redirect_response = input('Paste the full redirect URL here: ')
twitter.parse_authorization_response(redirect_response)

# Fetch the access token and store it as a dictionary
dict_file = twitter.fetch_access_token(access_token_url)



######################################################
#### Step 3: Storing the Keys in The YAML File #######
######################################################

# Load the current YAML file into Python as a dictionary
import bios
yaml_dict = bios.read('config.yaml')

# Pop out the twitter_api element, which is a dictionary within a dictionary
yaml_dict_new = yaml_dict.pop('twitter_api')

# Combine the current YAML dictionary with the dictionary with the access tokens from Step 2
d = dict_file.copy()
d.update(yaml_dict_new)

# Write the twitter_api key back into the new dictionary
d_final = {'twitter_api': d}

# Write the new dictionary into the YAML file in the directory
with open(r'config.yaml', 'w') as file:
    documents = yaml.dump(d_final, file)