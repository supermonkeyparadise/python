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

# [Step 2] Getting authorization by the user
#   Authorization means to give permission
#   [web workflow]
#       1. www.ourwebsite.com "log in with twitter button"
#       2. they press "Sign in" or "authorize"
#       3. Twitter sends them back e.q. www.ourwebsite.com/auth
#       4. We get that auth code + request token -> twitter -> access token
#

print('Go to the following site in your browser:')
print('{}?oauth_token={}'.format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

oauth_verifier = print('What is the PIN? ')
