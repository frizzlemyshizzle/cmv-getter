from bs4 import BeautifulSoup as bs
import json
import csv
import constants as con


#trn ID from overview - > Network -> Steam ID -> data -> metadata -> playerId

#History Data - https://api.tracker.gg/api/v1/rocket-league/player-history/mmr/<playerID>

# https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/<steamID>

linksList = [] #Start with empty list for tracker identifiers

with open('trackers.csv') as csvfile: #Opens Trackers input file
    count = 0 #Sets count to 0 to track number of entries in csv
    trackers = csv.reader(csvfile) #Defines CSV file as trackers
    for line in trackers: #For each line in csv file ->
        count += 1 #Add to count
        links = ''.join(line[2]) #Joins entries
        links = links.split('/', 7) # Removes redundatnt data from count of '/'
        links = links[6] # Sets links var as 6th index of variable (unique tracker ID)
        linksList = links.split("\n") # Adds each line from links var to list
        print(linksList)



steam_id = ''

profile_page = 'https://api.tracker.gg/api/v2/rocket-league/standard/profile/steam/'