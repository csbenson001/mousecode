import requests
import datetime as dt
from typing import List, Dict

from . import utils
from . import paths
from . import constants as c
from .objects import DiningOffer
from .database import get_db_connection

def get(url,alt_auth=False) -> requests.Response:
    resp = requests.get(url,headers=utils.get_auth_headers(alt_auth))
    return resp

def get_park(park_id: str) -> dict:
    url = (f'{c.APP_BASE}/explorer-service/public/finder/detail'
           f'/{park_id};entityType=theme-park')
    resp = requests.get(url,headers=utils.get_auth_headers())
    return resp.json()

def get_tipboard(park_id: str) -> dict:
    swid = ''
    with open(paths.USERID_TXT,'r+') as txtfile:
        swid = txtfile.read()
    url = utils.generate_tipboard_url(park_id,swid)
    headers = utils.get_auth_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()

def get_park_schedule(park_id: str, date: dt.date=None) -> dict:
    if date is None:
        date = dt.date.today().strftime(r'%Y-%m-%d')
    url = f'{c.APP_BASE}/facility-service/schedules/{park_id}?date={date}'
    resp = requests.get(url,headers=utils.get_auth_headers())
    return resp.json()

def get_dining_availability(restaurant_id:str,meal_period:str,party_size:int,search_date:str) -> dict:
    name = 'UNKNOWN'
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT name FROM Restaurants WHERE id=?",[restaurant_id])
    result = c.fetchall()[0]
    if len(result) != 0:
        name = result[0]
    conn.close()
    
    url = utils.generate_restaurant_url(restaurant_id,meal_period,party_size,search_date)
    headers = utils.get_auth_headers()
    resp = requests.get(url,headers=headers)
    availability = resp.json().get('availability',{})
    key = list(availability.keys())[0]
    available_times = availability[key].get('availableTimes',[{}])

    offers = [DiningOffer(name,o)
              for o in available_times[0].get('offers',[{}])]
    
    return offers

def get_park_dining_availability(park_id) -> dict:
    url = utils.generate_park_dining_url(park_id)
    headers = utils.get_dining_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()
    
def get_all_dining_availability(meal_period:str,party_size:str,search_date:str) -> dict:
    url = utils.generate_dining_check_url(meal_period,party_size,search_date)
    headers = utils.get_auth_headers()
    resp = requests.get(url,headers=headers)
    return resp.json()

