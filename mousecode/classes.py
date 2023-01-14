import json
import requests
import datetime as dt
# from dateutil.parser import parse

from .park import Park

from .constants import GO_BASE
from .constants import PRO_BASE
from .constants import APP_BASE
from .constants import AUTH_BASE
from .constants import AUTH_BASE_ALT
from .constants import HEADERS

from .paths import DATA_FOLDER_PATH
from .paths import INFO_FOLDER_PATH

from .utils import get_auth_token
from .utils import get_auth_headers
from .utils import generate_restaurant_url
from .utils import generate_dining_check_url



class MouseAPI:
    def __init__(self) -> None:
        self.__token: str
        self.__expires_at: dt.datetime
        self.__fetch_token_data()
        self.__headers = HEADERS
        
    def get_park(self,park_id:str,**kwargs) -> dict:
        url = (f'{APP_BASE}/explorer-service/public/finder/detail/'
               f'{park_id};entityType=theme-park')
        headers = self.__headers
        self.__check_auth()
        headers['Authorization'] = f'Bearer {self.__token}'
        if kwargs.get('log'):
            print(url)
        resp = requests.get(url,headers=headers)
        if kwargs.get('log'):
            with open('temp.json','w+') as jsonfile:
                json.dump(resp.json(),jsonfile)
        return Park.from_json(resp.json())
    
    def get_park_wait_times(self):
        ...
        
    def get_park_schedule(self,park_id:str, date:str=None) -> dict:
        if date is None:
            date = dt.date.today().strftime(r'%Y-%m-%d')
            
        url = f'{APP_BASE}/facility-service/schedules/{park_id}?date={date}'
        headers = self.__headers
        self.__check_auth()
        headers['Authorization'] = f'Bearer {self.__token}'
        
        resp = requests.get(url,headers=headers)
        return resp.json()
    
    def get_dining_availability(self,restaurant_id:str,meal_period:str,party_size:int,search_date:str) -> dict:
        url = generate_restaurant_url(restaurant_id,meal_period,party_size,search_date)
        
        headers = self.__headers
        self.__check_auth()
        headers['Authorization'] = f'Bearer {self.__token}'
        
        resp = requests.get(url,headers=headers)
        return resp.json()
    
    def get_all_dining_availability(self,meal_period:str,party_size:int,search_date:str) -> dict:
        url = generate_dining_check_url(meal_period,party_size,search_date)
        
        headers = self.__headers
        self.__check_auth()
        headers['Authorization'] = f'Bearer {self.__token}'
        
        resp = requests.get(url,headers=headers)
        return resp.json()

    def get_attraction(self,attraction_id:str):
        pass
    
    def __check_auth(self):
        try:
            if self.__time_left() < 15:
                self.__fetch_token_data()
        except:
            self.__fetch_token_data()
        
    def __time_left(self) -> int:
        expires_at = ""
        with open(f"{INFO_FOLDER_PATH}/token_expiration.txt","r") as txtfile:
            txt = txtfile.readlines()
            expires_at = txt[0].strip()
            
        return (dt.datetime.fromisoformat(expires_at) - dt.datetime.now()).seconds
            
    def __fetch_token_data(self,alt=False):
        if alt:
            url = f'{AUTH_BASE_ALT}'
            resp = requests.get(url,headers=HEADERS)
        else:
            params = {'grant_type':'assertion',
                      'assertion_type':'public',
                      'client_id':'WDPRO-MOBILE.MDX.WDW.ANDROID-PROD'}
            
            url = f"{AUTH_BASE}/token?"
            resp = requests.post(url,params=params)
        
        resp_json = resp.json()
        
        expires_in = resp_json.get('expires_in',0)
        token = resp_json.get('access_token','')
        self.__expires_at: dt.datetime = dt.datetime.now() + dt.timedelta(seconds=int(expires_in))
        self.__token: str = token
        
        with open(f"{INFO_FOLDER_PATH}/token_expiration.txt","w+") as txtfile:
            txtfile.write(f'{self.__expires_at}\n{self.__token}')
        