import requests
import datetime as dt
from typing import List, Dict

from .utils import get_auth_headers

from .constants import Base
from .constants import HEADERS
from .paths import SWID_KEY_TXT
from .paths import ATTRACTIONS_JSON
from .paths import ENTERTAINMENTS_JSON
from .paths import RESTAURANTS_JSON

def get_park(park_id: str) -> dict:
    url = f'{Base.APP}/explorer-service/public/finder/detail/{park_id};entityType=theme-park'
    resp = requests.get(url,headers=get_auth_headers())
    return resp.json()

def get_park_schedule(park_id: str, date: dt.date=None) -> dict:
    if date is None:
        date = dt.date.today().strftime(r'%Y-%m-%d')
    url = f'{Base.APP}/facility-service/schedules/{park_id}?date={date}'
    resp = requests.get(url,headers=get_auth_headers())
    return resp.json()

def get_swid() -> str:
    swid = ""
    with open(SWID_KEY_TXT,"r") as txtfile:
        swid = txtfile.read()
    return swid

