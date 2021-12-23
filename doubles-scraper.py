import http.client
from os import write
from re import T
import reader as r
import time
import constants as cons
import json
import datetime
from datetime import datetime, date
import csv

scrape = '2021-10-24'
count = 0
peakList = []


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
    if 'iJxG.?' in profile:
        trnIdentList.append('#######') ## Give empty ID
        historylinkList.append(cons.HIST_ENDP + '#######')
    else:
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




for link in historylinkList:

    ## Define Lists and reset each loop
    ratingDataList = []
    ratingList = []
    ratingDate = []
    holderList = []
    zonedRatingList = []

    if link[-1:] != '#':
        conn.request("GET", link, payload, headers) ## Hit ENDP
        res = conn.getresponse() ## Define response
        data = res.read() ## Read and define response
        x = json.loads(data) ## Load response to Json
        doublesRating = x['data']['11'] ## Fetch doubles rating from endpoint
        threesRating  = x['data']['13'] ## Fetch threes rating from endpoint

        for entry in doublesRating: ## For recorded mmr in twos ->
            ratingDate.append(entry['collectDate']) ## Add date to ratingDate list
            ratingList.append(entry['rating']) ## Add MMR to ratingList list

        for date in ratingDate: ## For each date in ratingDate list ->
            x = date[0:10] ## Take only the date (lazy way of remove time from datetime)
            ratingDataList.append(x) ## Add date to data list
            holderList.append(x) ## Holds all dates to process

        ratingDate = [datetime.strptime(date, '%Y-%m-%d').date() for date in holderList] ## Adjust rating date format
        for date in ratingDate: ## For each date in list ->
            if date >= datetime.date(datetime.strptime(scrape, '%Y-%m-%d')): ## If starting date >= to date in list -> 
                x = ratingDate.index(date) ## Store index of date as x
                zonedRatingList.append(ratingList[x]) ## Append the corresponding rating in ratingList
                peak = (zonedRatingList.index(max(zonedRatingList)))
                

  
        peakList.append(zonedRatingList[peak])

        with open('2s-output.csv', 'w', newline = '') as output:
            counter = 0
            peaks = [str(x) for x in peakList]
            writer = csv.writer(output)
            r.inputdataList[count].append(peaks[count])
            counter += 1
            for data in r.inputdataList:
                writer.writerow(data)
    print(str(count+1) + ' of ' + str(r.count) + ' processed')
    count +=1
    ### WRITE TO FAILED LINKS CSV ###
end = time.time()
print('EXECUTION TIME: ', end-start)
input('Press Enter to finish')

