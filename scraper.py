import http.client
import reader as r

trnIdent = []  ## Start with empty list for rltn identifiers
api_linksList = [] ## Start with empty list for api links
link = '/api/v2/rocket-league/standard/profile/' ## Link prefix

links = [link + ident for ident in r.identList]

for link in links:
    api_linksList.append(link)
print(api_linksList[2])



conn = http.client.HTTPSConnection("api.tracker.gg") ## Establish base of connection

payload = ""

headers = {
    'cookie': "X-Mapping-Server=s12; __cflb=02DiuFQAkRrzD1P1mdkJhfdTc9AmTWwYjUe5PNX8Y12aQ",
    'sec-ch-ua': "^\^",
    'Content-Type': "application/json"
    }

conn.request("GET", "/api/v2/rocket-league/standard/profile/steam/76561198197941479", payload, headers)

res = conn.getresponse()
data = res.read()


dataList = data.split(",".encode()) ## Transform data from page to list, entries seperated by ','

tracker_ident = (dataList[19].decode('utf-8')) ## Take 19th index of list (tracker ident)

trnIdent.append(tracker_ident[11:18]) ## Add Ident to trnIdent list