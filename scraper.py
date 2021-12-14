import http.client
from typing import Collection
import reader as r
import time
import constants as cons
import json


start = time.time()

trnIdentList = []  ## Start with empty list for rltn identifiers
historylinkList =[] ## Start with empty list for historic data links

conn = http.client.HTTPSConnection("api.tracker.gg") ## Establish base of connection

payload = ""

headers = {
    'cookie': "X-Mapping-Server=s12; __cflb=02DiuFQAkRrzD1P1mdkJhfdTc9AmTWwYjUe5PNX8Y12aQ",
    'sec-ch-ua': "^\^",
    'Content-Type': "application/json"
    }


for profile in r.prof_linksList: ## For each profile in list ->
    conn.request("GET", profile, payload, headers) ## Hit ENDP
    res = conn.getresponse() ## Define response
    data = res.read() ## Read and define response
    x = json.loads(data) ## Load response to Json
    if res.status == 200: ## If site response = 200 (OK)
        rltnId = x['data']['metadata']['playerId'] ## Take playerId from defined path
        trnIdentList.append(rltnId) ## Add id to list
        historylinkList.append(cons.HIST_ENDP + str(rltnId))
    else: ## If response not 200 ->
        trnIdentList.append('#######') ## Give empty ID
        historylinkList.append(cons.HIST_ENDP + '#######')

ratingList = []

for link in historylinkList:
    if link[-1:] != '#':
        conn.request("GET", link, payload, headers) ## Hit ENDP
        res = conn.getresponse() ## Define response
        data = res.read() ## Read and define response
        x = json.loads(data) ## Load response to Json
        doublesRating = x['data']['11']
        threesRating  = x['data']['13']
        print(link)
        ratingList.append(link)
        for entry in doublesRating:
            ratingList.append(entry['rating'])
            ratingList.append(entry['collectDate'])
    print(ratingList)
        

end = time.time()
print('EXECUTION TIME: ', end-start)
