import requests
import datetime as dt
from typing import List, Dict

from .utils import get_auth_headers
from .utils import generate_restaurant_url
from .utils import generate_dining_check_url
from .utils import generate_tipboard_url
from .constants import *

from .paths import SWID_KEY_TXT
from .paths import ATTRACTIONS_JSON
from .paths import ENTERTAINMENTS_JSON
from .paths import RESTAURANTS_JSON

def get(url,alt_auth=False) -> requests.Response:
    resp = requests.get(url,headers=get_auth_headers(alt_auth))
    return resp

def get_park(park_id: str) -> dict:
    url = f'{APP_BASE}/explorer-service/public/finder/detail/{park_id};entityType=theme-park'
    resp = requests.get(url,headers=get_auth_headers())
    return resp.json()

def get_tipboard(park_id: str) -> dict:
    url = generate_tipboard_url(park_id=park_id)
    headers = get_auth_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()

def get_park_schedule(park_id: str, date: dt.date=None) -> dict:
    if date is None:
        date = dt.date.today().strftime(r'%Y-%m-%d')
    url = f'{APP_BASE}/facility-service/schedules/{park_id}?date={date}'
    resp = requests.get(url,headers=get_auth_headers())
    return resp.json()

def get_dining_availability(restaurant_id:str,meal_period:str,party_size:int,search_date:str) -> dict:
    url = generate_restaurant_url(restaurant_id,meal_period,party_size,search_date)
    headers = get_auth_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()
    
def get_all_dining_availability(meal_period:str,party_size:str,search_date:str) -> dict:
    url = generate_dining_check_url(meal_period,party_size,search_date)
    headers = get_auth_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()
    
def __get_swid() -> str:
    swid = ""
    with open(SWID_KEY_TXT,"r") as txtfile:
        swid = txtfile.read()
    return swid

