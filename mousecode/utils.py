import requests

from .constants import Base
from .constants import HEADERS

def get_auth_headers() -> str:
    params = {'grant_type':'assertion',
              'assertion_type':'public',
              'client_id':'WDPRO-MOBILE.MDX.WDW.ANDROID-PROD'}
    
    url = f"{Base.AUTH}/token?"

    token = requests.post(url,params=params).json().get("access_token","")
    
    headers = HEADERS.copy()
    headers['Authorization'] = f'BEARER {token}'
    
    return headers