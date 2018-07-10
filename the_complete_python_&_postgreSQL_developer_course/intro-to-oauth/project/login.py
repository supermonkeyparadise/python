import oauth2
import constants
import urllib.parse as urlparse

# [Step 1] Getting the OAuth request token

# identify the app
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)

response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('An error occurred getting the request token from Twitter!')

# convert the query str into a dictionary
request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
