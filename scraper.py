from bs4 import BeautifulSoup as bs
import json
import csv
import constants as con


#trn ID from overview - > Network -> Steam ID -> data -> metadata -> playerId

#History Data - https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/<playerID>

# https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/<steamID>


dataList = [] ## Start with empty list for tracker identifiers ##
linksList = [] ## Start with empty list for trackers



with open('trackers.csv') as csvfile: ## Opens Trackers input file ##
    count = 0 ## Set count to track number of entries ##
    trackers = csv.reader(csvfile) ## Defines file as 'trackers' ##

    for row in trackers: ## For every row in trackers ##
        dataList.append(row[0:3]) ## Add to list [0]RSC ID, [1]Name, [2]Link ##
        count += 1 ## Add 1 to count for each row ##
    print(str(count) + ' ENTRIES IN FILE')

    for data in dataList:
        linksList.append(data[2]) ## Add trackers links to links list ##



steam_id = ''

profile_page = 'https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/'