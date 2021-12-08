from bs4 import BeautifulSoup as bs
import json
import csv
import constants as con


#trn ID from overview - > Network -> Steam ID -> data -> metadata -> playerId

#History Data - https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/<playerID>

# https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/<steamID>


dataList = [] ## Start with empty list for tracker identifiers
linksList = [] ## Start with empty list for trackers
identList = [] ## Start with empty list for idents (Steam ID / player name if console)




with open('trackers.csv') as csvfile: ## Opens Trackers input file
    count = 0 ## Set count to track number of entries
    trackers = csv.reader(csvfile) ## Defines file as 'trackers'

    for row in trackers: ## For every row in trackers ->
        dataList.append(row[0:3]) ## Add to data list -> [0]RSC ID,[1]Name,[2]Link ([start:end-1]) 
        count += 1 ## Add 1 to count
    print(str(count) + ' ENTRIES IN FILE \n')

    for data in dataList: ## For every entry in data List ->
        linksList.append(data[2]) ## Add trackers links to links list

    for links in linksList: ## For every link in link list ->
        ident = links.split('/', 7) ## Remove link info (Counts # of '/'), keep identifiers
        identList.append(ident[6]) ## Add identifiers to indentifier list

        




steam_id = ''

profile_page = 'https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/'