# scripts/oauth_auth.py

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def authenticate():
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://provider.com/oauth/token', client_id=client_id, client_secret=client_secret)
    return oauth
