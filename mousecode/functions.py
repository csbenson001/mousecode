import requests
from typing import List, Dict

from .constants import Base
from .constants import HEADERS
from .paths import SWID_KEY_TXT

def get_park_attractions(park_id) -> dict:
    headers = HEADERS
    headers["Authorization"] = f"BEARER {get_auth()}"
    url = f'{Base.app}/facility-service/attractions/{park_id}?region=us'
    resp = requests.get(url,headers=headers)
    return resp.json()

def get_auth() -> str:
    url = f"{Base.auth}/token?grant_type=assertion&assertion_type=public&client_id=WDPRO-MOBILE.MDX.WDW.ANDROID-PROD"

    return requests.post(url).json().get("access_token","")

def get_swid() -> str:
    swid = ""
    with open(SWID_KEY_TXT,"r") as txtfile:
        swid = txtfile.read()
    return swid

