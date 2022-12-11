import time
import datetime as dt
from typing import List, Dict, Union, Optional, Tuple

import pandas as pd

from . import utils
from . import functions as funcs
from .database import get_db_connection

class Park:
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        descs = kwargs.get('descriptions',{})
        desc = (descs.get('description',descs.get('shortDescription',{})))
        self.description = desc.get('sections',{}).get('title')
        self.hours = self.__park_hours(kwargs)
        self.entrance = self.__guest_entrance_coords(kwargs)
        
    def check_tipboard(self,**kwargs):
        """Fetches the posted wait times for park attractions (As 
        seen on the MDE Tipboard)
        """
        _resp = funcs.get_tipboard(self.id)
        if kwargs.get('return_all'):
            return _resp
        data = []
        conn = get_db_connection()
        c = conn.cursor()
        statement = "SELECT name FROM Attractions WHERE id=?"
        for entry in _resp.get('availableExperiences',[{}]):
            c.execute(statement,[entry.get('id','')])
            result = c.fetchone()
            name = None
            is_attraction = False
            is_entertainment = False
            if result is None:
                c.execute(statement,[entry.get('id','')])
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
        
    def check_dining(self,**kwargs):
        """Fetches the park's current dining availability"""
        _resp = funcs.get_park_dining_availability(self.id)
        if kwargs.get('return_all'):
            return _resp
        data = []
        available_dining = _resp.get('availableDining',[{}])
        conn = get_db_connection()
        c = conn.cursor()
        
        statement = 'SELECT name FROM Restaurants WHERE id=?'
        
        for entry in available_dining:
            c.execute(statement,[entry.get('id','')])
            result = c.fetchone()
            if len(result) == 0:
                continue
            else:
                name = result[0]
            mobile_order = entry.get('mobileOrder',{})
            mobile_order_available = mobile_order.get('available',False)
            _mobile_next = mobile_order.get('nextAvailableTime',{})
            if _mobile_next == {}:
                next_mobile_order_window = 'NOT_AVAIL'
            else:
                mobile_start = _mobile_next.get('displayStartTime')
                mobile_end = _mobile_next.get('displayEndTime')
                next_mobile_order_window = f'{mobile_start} - {mobile_end}'
            
            walkup = entry.get('walkup',{})
            walkup_available = walkup.get('available',False)
            walkup_wait = str(walkup.get('waitTime','NOT_AVAIL'))
            
            dine = entry.get('dine',{})
            dine_available = dine.get('available',False)
            dine_next_time = str(dine.get('displayNextAvailableTime',
                                          'NOT_AVAIL'))
            
            data.append({
                'id': entry.get('id'),
                'type': entry.get('type'),
                'name': name,
                # 'mobile_order_available': mobile_order_available,
                'mobile_order_window': next_mobile_order_window,
                # 'walkup_available': walkup_available,
                'walkup_wait': walkup_wait,
                # 'dine_available': dine_available,
                'dine_next_time': dine_next_time,
            })
        
        conn.close()
        
        df = pd.DataFrame(data)
        return df
            
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
    
    @classmethod
    def from_json(cls,d):
        return cls(**d)