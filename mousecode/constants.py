GO_BASE  = "https://disneyworld.disney.go.com"
GO_API   = "https://disneyworld.disney.go.com/api/wdpro"
PRO_BASE = "https://api.wdpro.disney.go.com"
APP_BASE = "https://api.wdprapps.disney.com"
AUTH_BASE = "https://authorization.go.com/token"
AUTH_BASE_ALT = "https://disneyworld.disney.go.com/authentication/get-client-token/"

MAGIC_KINGDOM      = "80007944"
EPCOT              = "80007838"
HOLLYWOOD_STUDIOS  = "80007998"
ANIMAL_KINGDOM     = "80007823"

BREAKFAST = '80000712'
BRUNCH    = '80000713'
LUNCH     = '80000717'
DINNER    = '80000714'

HEADERS = {
    'Accept-Language' : 'en_US',
    'Cache-Control' : '0',
    'User-Agent': 'UIEPlayer/2.1 iPhone OS 6.0.1',
    'Accept' : 'application/json;apiversion=1',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Connection' : 'keep-alive',
    'x-UJinn-Devcap' : '2048,1496,true,32',
    'x-UJinn-Copyright' : 'Copyright UIEvolution Inc.',
    'Proxy-Connection' : 'keep-alive',
    'Content-Length' : '77',
    'Accept-Encoding' : 'gzip, deflate'
    }


"""
url = f'https://disneyworld.disney.go.com/tipboard-vas/api/v1/parks/{t.MK}/experiences?userId={userId}'
url = f'https://api.wdprapps.disney.com/explorer-service/public/finder/detail/80007944;entityType=theme-park'
url = f'https://api.wdprapps.disney.com/facility-service/menu-items/240323?region=us'
"""