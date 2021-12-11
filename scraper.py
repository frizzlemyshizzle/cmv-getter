import http.client
import reader as r

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
    data = res.read().split(",".encode())
    dataList = data ## Transform data from page to list, entries seperated by ','

    print(dataList)
    print('####################NEXT PLAYER ############################')
    dataList.clear()

##tracker_ident = (dataList[19].decode('utf-8')) ## Take 19th index of list (tracker ident)

##trnIdentList.append(tracker_ident[11:18]) ## Add Ident to trnIdent list
