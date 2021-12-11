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


for profile in r.prof_linksList:
    conn.request("GET", profile, payload, headers)
    res = conn.getresponse()
    data = res.read()
    x = str(data)
    if 'playerId' in x: ## If 'playerId' string in data ->
        ind = x.index('playerId') ## Get index for beginning of 'playerID'
        ind1 = x[ind+10:ind+16] ## Iterate over start index + 10 to remove playerID string and retrieve just ID
        trnIdentList.append(ind1) ## Add ID to list

        ## THIS METHOD IS REALLY SLOW, QUICKER METHODS REQ

print(trnIdentList)
print('####################################################')

end = time.time()
print('EXECUTION TIME: ', end-start)
##tracker_ident = (dataList[19].decode('utf-8')) ## Take 19th index of list (tracker ident)

##trnIdentList.append(tracker_ident[11:18]) ## Add Ident to trnIdent list
