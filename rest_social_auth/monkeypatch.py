from social_core.backends.oauth import BaseOAuth1


def get_unauthorized_token(self):
    return {
        'oauth_token': self.data.get('oauth_token'),
        'oauth_token_secret': self.data.get('oauth_token_secret')
    }


BaseOAuth1.get_unauthorized_token = get_unauthorized_token
