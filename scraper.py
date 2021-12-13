import http.client
import reader as r
import time
import constants as cons
import json


start = time.time()

trnIdentList = []  ## Start with empty list for rltn identifiers
historylinkList =[]

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
    data = res.read()
    x = json.loads(data)
    if res.status == 200:
        rltnId = x['data']['metadata']['playerId']
        trnIdentList.append(rltnId)
    else:
        trnIdentList.append('#######')
print(trnIdentList)
historylinkList = [cons.HIST_ENDP + ident for ident in trnIdentList]

end = time.time()
print('EXECUTION TIME: ', end-start)
