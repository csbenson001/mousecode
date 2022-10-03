from codecs import getdecoder
import datetime as dt
from symbol import continue_stmt
from typing import List, Dict, Union, Optional, Tuple

import pandas as pd

from . import functions as funcs
from .database import get_db_connection

class Park:
    def __init__(self,d:dict):
        self.id = d.get('id')
        self.name = d.get('name')
        self.type = d.get('type')
        descs = d.get('descriptions',{})
        self.description = (descs.get('shortDescription',descs.get('description')))
        self.park_hours = self.__park_hours(d)
        self.guest_entrance = self.__guest_entrance_coords(d)
        
    def tipboard(self):
        _resp = funcs.get_tipboard(self.id)
        data = []
        conn = get_db_connection()
        c = conn.cursor()
        for entry in _resp.get('availableExperiences',[{}]):
            c.execute("SELECT name FROM Attractions WHERE id=?",
                      [entry.get('id','')])
            result = c.fetchone()
            name = None
            is_attraction = False
            is_entertainment = False
            if result is None:
                c.execute("SELECT name FROM Entertainments WHERE id=?",[entry.get('id','')])
                result = c.fetchone()
                if result is not None:
                    is_entertainment = True
                    name = result[0]
            else:
                is_attraction = True
                name = result[0]
            if (name is not None) and (is_attraction or is_entertainment):
                is_show = True if 'additionalShowTimes' in entry.keys() else False
                is_individual = True if 'individual' in entry.keys() else False
                
                standby = entry.get('standby')
                standby_wait = None
                next_show = None
                showtimes = None
                if standby is not None:
                    if is_show:
                        next_show = standby.get('displayNextShowTime')
                        showtimes = entry.get('displayAdditionalShowTimes')
                    else:
                        standby_wait = standby.get('waitTime') 
                
                genie = entry.get('flex',entry.get('individual'))
                genie_next = None
                genie_price = None
                if genie is not None:
                    genie_next = genie.get('displayNextAvailableTime')
                    genie_price = genie.get('displayPrice')
                    
                data.append({
                    'id':entry.get('id',''),
                    'type':entry.get('type',''),
                    'name':name,
                    'standby_wait':standby_wait,
                    'next_ll':genie_next,
                    'price_ll':genie_price,
                    'next_show':next_show,
                    'showtimes':showtimes,
                    'is_individual':is_individual,
                    'is_show':is_show,
                })
                
        df = pd.DataFrame(data)
        return df
        
    def dining_availability(self):
        pass
    
    def __park_hours(self,d):
        data = d.get('schedule',{}).get('schedules',[{}])
        for d in data:
            d['start_time'] = d.pop('startTime')
            d['end_time'] = d.pop('endTime')
        df = pd.DataFrame(data)
        return df
    
    def __guest_entrance_coords(self,d) -> Tuple[str,str]:
        gps = d.get('coordinates',{}).get('Guest Entrance',{}).get('gps',{})
        return (gps.get('latitude'), gps.get('longitude'))