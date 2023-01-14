import requests, pprint

from flask import Flask, request
from flask.json import jsonify
import pyperclip as pyp

import mousecode as mc
from mousecode import restaurant_ids as r
from mousecode import BREAKFAST, LUNCH, DINNER
from mousecode.constants import MAGIC_KINGDOM, EPCOT, HOLLYWOOD_STUDIOS, ANIMAL_KINGDOM
from mousecode.utils import generate_restaurant_url, generate_dining_check_url, generate_park_dining_url
from mousecode.utils import rich, get_auth_token, get_auth_headers, get_dining_headers
from mousecode.objects import DiningOffer
from mousecode.functions import get_dining_availability, get_restaurant_name

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def debug():
    rid = r.CAPE_MAY_CAFE
    meal_time = BREAKFAST + ";" + DINNER
    party = 3
    date = "2023-03-01"
    
    url = generate_restaurant_url(rid,meal_time,party,date)
    url = generate_dining_check_url(meal_time,party,date)
    # url = generate_park_dining_url(MAGIC_KINGDOM, date)
    
    name = get_restaurant_name(rid)
    headers = get_auth_headers()
    headers["Authorization"] = f"BEARER b72cfd6a87014e788665c0e3fafe19c2"
    token = headers["Authorization"].replace("Bearer","").strip()
    
    with requests.session() as sesh:
        url = "https://disneyworld.disney.go.com"
        resp = sesh.get(url,headers=headers,allow_redirects=False)
        url = "https://disneyworld.disney.go.com/finder/api/v1/explorer-service/list-ancestor-entities/wdw/80007798;entityType=destination/2023-01-10/dining"
        resp = sesh.get(url,headers=headers,allow_redirects=False)
        
    try:
        d = resp.json()
        # d = dict(resp.headers)
        return jsonify(d)
    except Exception as e:
        print(e)
        return resp.content

host = "127.0.0.1"
port = 5500
if __name__ == "__main__":
    r.SAN_ANGEL_INN
    r.CINDERELLAS_ROYAL_TABLE
    r.CHEF_MICKEYS
    r.SCIFI_DINE_IN
    # mc.get_dining_availability()
    ...
    # pyp.copy(f"{host}:{port}")
    # app.run(host,port=port,debug=True)