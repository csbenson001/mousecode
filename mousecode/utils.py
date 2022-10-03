import requests

from . import paths
from . import constants as c

def get_auth_headers(alt=False) -> dict:
    headers = c.HEADERS
    
    if alt:
        url = f'{c.AUTH_BASE_ALT}'
        resp = requests.get(url,headers=headers)
        token = resp.json()['access_token']
        headers['Authorization'] = f'Bearer {token}'
    else:
        params = {'grant_type':'assertion',
                  'assertion_type':'public',
                  'client_id':'WDPRO-MOBILE.MDX.WDW.ANDROID-PROD'}
        
        url = f"{c.AUTH_BASE}/token?"
        token = requests.post(url,params=params).json().get("access_token","")
        headers['Authorization'] = f'Bearer {token}'
        
    return headers

def get_headers() -> dict:
    return c.HEADERS

def get_auth_token(alt:bool=False) -> str:
    if alt:
        resp = requests.get(c.AUTH_BASE_ALT,headers=c.HEADERS)
        token = resp.json().get('access_token','')
    else:
        params = {'grant_type':'assertion',
                  'assertion_type':'public',
                  'client_id':'WDPRO-MOBILE.MDX.WDW.ANDROID-PROD'}
        
        url = f"{c.AUTH_BASE}/token?"
        token = requests.post(url,params=params).json().get("access_token","")
    return token

def generate_restaurant_url(restaurant_id:str,meal_period:str,party_size:int,search_date:str) -> str:
    path = f"/dining-availability/{restaurant_id};entityType=restaurant"
    url = c.PRO_BASE + f"/explorer-service/public/v2/finder{path}"
    params = {'mealPeriod':meal_period,'partySize':party_size,'searchDate':search_date}
    req = requests.Request("GET",url,params=params)
    
    return req.prepare().url

def generate_dining_check_url(meal_period:str,party_size:str,search_date:str) -> str:
    path = "dining-availability/80007798;entityType=destination"
    url = f"{c.PRO_BASE}/explorer-service/public/v2/finder/{path}?"
    
    params = {'includePrePaid': 'true',
              'groupOffersByProduct': 'true',
              'searchDate': search_date,
              'mealPeriod': meal_period,
              'partySize': party_size
              }
    
    req = requests.Request("GET",url,params=params)
    url = req.prepare().url
    return url

def get_swid():
    swid = ''
    with open(paths.SWID_KEY_TXT,'r+') as txtfile:
        swid = txtfile.read()
    return swid

def generate_tipboard_url(park_id:str,userId:str) -> str:
    path = f"{c.GO_BASE}/tipboard-vas/api/v1/parks/{park_id}/experiences"
    return f"{path}?userId={userId}"