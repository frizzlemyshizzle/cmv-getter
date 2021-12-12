import http.client
import reader as r
import time

start = time.time()

trnIdentList = []  ## Start with empty list for rltn identifiers

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
    x = str(data)
    if res.status == 200: ## If link is found ->
        print(True)
        if 'playerId' in x: ## If 'playerId' string in data ->                              ####################
            ind = x.index('playerId') ## Get index for beginning of 'playerID'              ## THIS METHOD IS ##
            ind1 = x[ind+10:ind+16] ## Start index + 10 to remove playerID, return ID       ##  REALLY SLOW!  ##
            trnIdentList.append(ind1) ## Add ID to list                                     ####################   
    else: ## If link is not found ->
        trnIdentList.append("Link not found")


 

print(trnIdentList)
print('####################################################')
end = time.time()
print('EXECUTION TIME: ', end-start)
