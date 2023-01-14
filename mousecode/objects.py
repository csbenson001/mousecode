import datetime as dt
from typing import List, Dict, Union
from collections import UserList

class DiningOffer:
    def __init__(self,name:str,offer_dict:Dict,party_size:int):
        time = offer_dict['time']
        datetime = offer_dict['dateTime']
        self.name: str = name
        self.datetime: dt.datetime = (dt.datetime
                                      .strptime(datetime,r'%Y-%m-%dT%H:%M:%S%z'))
        self.date: dt.date = self.datetime.date()
        self.time = (dt.datetime.strptime(time,r'%H:%M')
                     .strftime(r'%I:%M %p'))
        
        self.dow: str = self.date.strftime(r'%a')
        self.month_short: str = self.date.strftime(r'%b')
        self.day: str = self.date.strftime(r'%d')
        self.party_size = party_size
        
    def __repr__(self) -> str:
        dow = self.datetime.strftime(r'%a')
        month = self.datetime.strftime(r'%B')
        day = self.datetime.strftime(r'%d')
        year = self.datetime.year
        return f'DiningOffer({self.name}: {self.time}, {dow} {month} {day} {year})'