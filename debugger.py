import pprint

from flask import Flask, request
from flask.json import jsonify
import pyperclip as pyp

from mousecode import restaurant_ids as r
from mousecode.utils import generate_restaurant_url
from mousecode.utils import get_auth_headers
from mousecode.objects import DiningOffer
from mousecode.functions import get_dining_availability, get_restaurant_name, _extract_offers
from mousecode.asyncfetch import runit as fetchall
from urllib.parse import unquote_plus, parse_qs

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def debug():
    headers = get_auth_headers()
    urls = [
        generate_restaurant_url(r.BIERGARTEN_RESTAURANT,"2:00 PM", 3, "2023-02-10"),
        generate_restaurant_url(r.BIERGARTEN_RESTAURANT,"8:00 PM", 3, "2023-01-30"),
        generate_restaurant_url(r.SAN_ANGEL_INN,"2:00 PM", 3, "2023-02-20")
    ]
    url = urls[0]
    print(unquote_plus(url))
    print(parse_qs(url))
    headers = get_auth_headers()
    responses = fetchall(urls,headers)
    return jsonify(responses)
    
host = "127.0.0.1"
port = 5500
if __name__ == "__main__":
    # r.SAN_ANGEL_INN
    # r.CINDERELLAS_ROYAL_TABLE
    # r.CHEF_MICKEYS
    # r.SCIFI_DINE_IN
    # mc.get_dining_availability()
    pyp.copy(f"{host}:{port}")
    app.run(host,port=port,debug=True)