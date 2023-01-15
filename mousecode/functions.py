import requests
from urllib.parse import parse_qs, unquote_plus
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

def get_dining_availability(restaurant_id:str,time:str,party_size:int,date:str,**kwargs) -> List[DiningOffer]:
    name = 'UNKNOWN'
    headers = kwargs.get("headers")
    
    if not kwargs.get("name"):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT name FROM Restaurants WHERE id=?",[restaurant_id])
        result = c.fetchall()[0]
        if len(result) != 0:
            name = result[0]
        conn.close()
    else:
        name = kwargs.get("name")
    
    url = utils.generate_restaurant_url(restaurant_id,time,party_size,date)
    
    if not headers:
        headers = utils.get_auth_headers()
    
    resp = requests.get(url,headers=headers)

    if kwargs.get("debug"):
        print(url)
        print(headers['Authorization'])
        try:
            print(resp.json())
        except:
            pass

    offers = _extract_offers(resp.json(), party_size)
    
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

def get_restaurant_name(restaurant_id:str):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT name FROM Restaurants WHERE id=?;",[restaurant_id])
    result = c.fetchall()[0]
    if len(result) != 0:
        name = result[0]
    conn.close()
    return name

rich = utils.rich
def _extract_offers(resp_json:Dict,url:str):
    availability = resp_json.get('availability',{})
    key = list(availability.keys())[0]
    available_times = availability[key].get('availableTimes',[{}])
    
    query = url[url.find("?")+1:]
    restaurant_id = url[url.rfind("/") + 1:url.find(";entity")]
    params = parse_qs(query)

    offers = []
    if available_times[0].get("offers"):
        for offer in available_times[0]["offers"]:
            offer["datetime"] = offer.pop("dateTime")
            offer["party_size"] =  params["partySize"][0]
            offer["offer_id"] = offer["url"][offer["url"].rfind("/")+1:]
            offer["restaurant_id"] = restaurant_id
            offers.append(offer)
            # offers.append(DiningOffer(name,offer,party_size))
    return offers








