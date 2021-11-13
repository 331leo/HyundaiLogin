from os import getenv


def generate_oauth_link() -> str:
    """
    Generates a link to the OAuth2 authorization page.
    """
    return (
        f"https://accounts.google.com/o/oauth2/v2/auth?prompt=consent&"
        f"response_type=code&client_id={getenv('GOOGLE_CLIENT_ID')}&"
        f"scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid&"
        f"access_type=offline&hd={getenv('GOOGLE_FIXED_HD')}&redirect_uri={getenv('GOOGLE_REDIRECT_URI')}"
    )
