import datetime as dt
from typing import List, Dict, Union
from collections import UserList

class DiningOffer:
    def __init__(self,name:str,offer_dict:Dict):
        time = offer_dict['time']
        datetime = offer_dict['dateTime']
        self.name: str = name
        self.datetime: dt.datetime = (dt.datetime
                                      .strptime(datetime,r'%Y-%m-%dT%H:%M:%S%z'))
        self.time = (dt.datetime.strptime(time,r'%H:%M')
                     .strftime(r'%I:%M %p'))
        
    def __repr__(self) -> str:
        dow = self.datetime.strftime(r'%a')
        month = self.datetime.strftime(r'%B')
        day = self.datetime.strftime(r'%d')
        year = self.datetime.year
        return f'DiningOffer({self.name}: {self.time}, {dow} {month} {day} {year})'