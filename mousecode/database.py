import json
import sqlite3
from typing import List, Dict, Tuple

import pandas as pd

from . import paths

def get_db_connection():
    return sqlite3.connect(f'{paths.DATA_FOLDER_PATH}/mouse.db')

def get_results_and_cols(_cursor:sqlite3.Cursor):
    return (_cursor.fetchall(),[_[0] for _ in _cursor.description])

def map_results(_data:List[Tuple],_cols):
    mapped_data = []
    col_mapper = {col:idx for idx,col in enumerate(_cols)}
    for entry in _data:
        mapped_entry = {}
        for col,idx in col_mapper.items():
            mapped_entry[col] = entry[idx]
        mapped_data.append(mapped_entry)
    return mapped_data

def map_results_from_cursor(_cursor:sqlite3.Cursor):
    return map_results(*get_results_and_cols(_cursor))

class db:
    def __init__(self):
        pass
    
    def restaurants(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM Restaurants")
        mapped_data = map_results_from_cursor(c)
        df = pd.DataFrame(mapped_data)
        for c in ('price_range','table_service','cuisine'):
            df[c] = df[c].apply(lambda x: json.loads(x))
        conn.close()
        return df

    def attractions(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM Attractions")
        mapped_data = map_results_from_cursor(c)
        df = pd.DataFrame(mapped_data)
        for c in ('age','height','thrills'):
            df[c] = df[c].apply(lambda x: json.loads(x))
        conn.close()
        return df
    
    def entertainments(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM Entertainments")
        mapped_data = map_results_from_cursor(c)
        df = pd.DataFrame(mapped_data)
        for c in ('age','age_groups','interests','park_interests','entertainment_types'):
            df[c] = df[c].apply(lambda x: json.loads(x))
        conn.close()
        return df

    dining = restaurants

class init_db:
    
    def restaurants():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Restaurants")
        c.execute("""
                  CREATE TABLE IF NOT EXISTS Restaurants (
                      id PRIMARY_KEY TEXT,
                      name TEXT,
                      price_range TEXT,
                      table_service TEXT,
                      lat TEXT,
                      lon TEXT,
                      cuisine TEXT,
                      desc TEXT,
                      img TEXT,
                      theme_park TEXT,
                      water_park TEXT,
                      resort_area TEXT,
                      land TEXT
                  )
                  """)
        with open(paths.RESTAURANTS_JSON,'r+') as jsonfile:
            data = json.load(jsonfile)
            params = []
            for entry in data:
                params.append([
                    entry['id'],
                    entry['name'],
                    json.dumps(entry['price_range']),
                    json.dumps(entry['table_service']),
                    entry['lat'],
                    entry['lon'],
                    json.dumps(entry['cuisine']),
                    entry['desc'],
                    entry['img'],
                    entry['theme-park'],
                    entry['water-park'],
                    entry['resort-area'],
                    entry['land'],
                    ]
                )
            phs = f'{",".join("?"*13)}'
            statement = f"INSERT INTO Restaurants VALUES({phs})"
            c.executemany(statement,params)
        
        conn.commit()
        conn.close()
    
    def attractions():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Attractions")
        c.execute("""
                  CREATE TABLE IF NOT EXISTS Attractions (
                      id PRIMARY_KEY TEXT,
                      name TEXT,
                      age TEXT,
                      height TEXT,
                      lat TEXT,
                      lon TEXT,
                      thrills TEXT,
                      desc TEXT,
                      img TEXT,
                      theme_park TEXT,
                      water_park TEXT,
                      resort_area TEXT,
                      land TEXT
                  )
                  """)
        with open(paths.ATTRACTIONS_JSON,'r+') as jsonfile:
            data = json.load(jsonfile)
            params = []
            for entry in data:
                params.append([
                    entry['id'],
                    entry['name'],
                    json.dumps(entry['age']),
                    json.dumps(entry['height']),
                    entry['lat'],
                    entry['lon'],
                    json.dumps(entry['thrills']),
                    entry['desc'],
                    entry['img'],
                    entry['theme-park'],
                    entry['water-park'],
                    entry['resort-area'],
                    entry['land'],
                ])
            phs = f'{",".join("?"*13)}'
            statement = f"INSERT INTO Attractions VALUES({phs})"
            c.executemany(statement,params)
            
        conn.commit()
        conn.close()

    def entertainments():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS Entertainments")
        c.execute("""
                  CREATE TABLE IF NOT EXISTS Entertainments (
                      id PRIMARY_KEY TEXT,
                      name TEXT,
                      age TEXT,
                      age_groups TEXT,
                      entertainment_types TEXT,
                      interests TEXT,
                      park_interests TEXT,
                      lat TEXT,
                      lon TEXT,
                      desc TEXT,
                      img TEXT,
                      theme_park TEXT,
                      water_park TEXT,
                      resort_area TEXT,
                      land TEXT
                  )
                  """)
        
        with open(paths.ENTERTAINMENTS_JSON,'r+') as jsonfile:
            data = json.load(jsonfile)
            params = []
            for entry in data:
                params.append([
                    entry['id'],
                    entry['name'],
                    json.dumps(entry['age']),
                    json.dumps(entry['age_groups']),
                    json.dumps(entry['entertainment_types']),
                    json.dumps(entry['interests']),
                    json.dumps(entry['park_interests']),
                    entry['lat'],
                    entry['lon'],
                    entry['desc'],
                    entry['img'],
                    entry['theme-park'],
                    entry['water-park'],
                    entry['resort-area'],
                    entry['land'],
                ])
            phs = f'{",".join("?"*15)}'
            statement = f"INSERT INTO Entertainments VALUES({phs})"
            c.executemany(statement,params)
        
        conn.commit()
        conn.close()

    dining = restaurants