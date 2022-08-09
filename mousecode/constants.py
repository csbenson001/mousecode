
GO_BASE  = "https://disneyworld.disney.go.com"
GO_API   = "https://disneyworld.disney.go.com/api/wdpro"
PRO_BASE = "https://api.wdpro.disney.go.com"
APP_BASE = "https://api.wdprapps.disney.com"
AUTH_BASE = "https://authorization.go.com/token"
# AUTH_BASE_ALT = "https://disneyworld.disney.go.com/authentication/get-client-token/"


"""
url = f'https://disneyworld.disney.go.com/tipboard-vas/api/v1/parks/{t.MK}/experiences?userId={userId}'
url = f'https://api.wdprapps.disney.com/explorer-service/public/finder/detail/80007944;entityType=theme-park'
url = f'https://api.wdprapps.disney.com/facility-service/menu-items/240323?region=us'
"""

class ParkId:
    MAGIC_KINGDOM = "80007944"
    EPCOT = "80007838"
    HOLLYWOOD_STUDIOS = "80007998"
    ANIMAL_KINGDOM = "80007823"

class Base:
    go = GO_BASE
    goapi = GO_API
    pro = PRO_BASE
    app = APP_BASE
    auth = AUTH_BASE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0"}