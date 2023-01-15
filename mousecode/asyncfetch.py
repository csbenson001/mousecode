import asyncio, aiohttp, nest_asyncio
from typing import Union, List, Dict, Optional
from urllib.parse import parse_qs, unquote_plus

from mousecode.functions import _extract_offers

nest_asyncio.apply()

def _determine_loop():
    try:
        return asyncio.get_event_loop()
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return asyncio.get_event_loop()

class FetchedResponse:
    def __init__(self,_url,_headers,_json) -> None:
        self.url: str = _url
        self.headers: dict = _headers
        self.json: dict = _json

async def fetch(urls:List,headers:Dict):
    retrieved_responses = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(session.get(url, ssl=True, headers=headers))

        responses = await asyncio.gather(*tasks)
        
        for response in responses:
            resp_url = str(response.url)
            # resp_headers = dict(response.headers)
            resp_json: Dict = await response.json()
            
            offers = _extract_offers(resp_json,resp_url)
            for o in offers:
                retrieved_responses.append(o)
            
            # sync_resp = resp_json
            # sync_resp = FetchedResponse(resp_url,resp_headers,resp_json)
            # retrieved_responses.append(sync_resp)
        
        await session.close()
    
    return retrieved_responses

def runit(urls:List,headers:Dict,**kwargs):# -> List[FetchedResponse]:
    loop = _determine_loop()
    retrieved = loop.run_until_complete(fetch(urls,headers))
    return retrieved
