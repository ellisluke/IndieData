# IMPORTS

import requests
import instaloader
from bs4 import BeautifulSoup
import re
import pandas as pd

### HANDLE DATA ###

def refreshData(ig, yt, sp, ap):
    # Update usernames in ScrapeLinks.csv
    linkData = [ig, yt, sp, ap]
    linkDf = pd.DataFrame(linkData, index=['Instagram', 'YouTube', 'Spotify', 'Apple Music'], columns=['Platform', 'Link'])
    linkDf.to_csv("ScrapeLinks.csv")
    # Fetch current stats using retrieve functions

    # Put new stats in data CSV


# Useful function
# Purpose is to whittle down the scraping results to just the nth occurence of a desired HTML tag
# tag = name of tag you wish to find
# n = index of desired tag result
def find_nth_tag(soup, tag, n):
    tags = soup.find_all(tag)
    # Helper to find your target tag
    j = 0
    # for t in tags:
    #     print("NUMBER: ", j, " ", t)
    #     j = j+1
    if len(tags) >= n:
        return tags[n]
    else:
        return None

# FUNCTIONS TO GET DATA FROM LINKS

# Instagram Profile data using instagramy
def instagramRetrieve(username):
    L = instaloader.Instaloader()
    IGProfile = instaloader.Profile.from_username(L.context, username) # https://instaloader.github.io/module/structures.html#instaloader.Profile.followers
    return IGProfile.followers

# # Youtube Channel data using BeautifulSoup web scraping
def youtubeRetrieve(channelLink):
    youtubeGet = requests.get(channelLink)
    youtubeSoup = BeautifulSoup(youtubeGet.text, 'html.parser')
    targetScriptTag = str(find_nth_tag(youtubeSoup, "script", 36))
    ytRePattern = '"content":"(\d+) subscribers"'
    ytMatches = re.findall(ytRePattern, targetScriptTag)
    if ytMatches:
        currentSubscribers = int(ytMatches[0])
        return currentSubscribers
    else:
        print("No YouTube match found :(")
        return 0


# Spotify Artist data using BeautifulSoup web scraping
def spotifyRetrieve(artistLink):
    spotifyGet = requests.get(artistLink)
    spotifySoup = BeautifulSoup(spotifyGet.text, 'html.parser')
    targetMetaTag = str(find_nth_tag(spotifySoup, "meta", 6))
    spotifyRePattern = '(\d+) monthly listeners.'
    spotifyMatches = re.findall(spotifyRePattern, targetMetaTag)

    if spotifyMatches:
        currentMonthlyListeners = int(spotifyMatches[0])
        print(currentMonthlyListeners)
    else: 
        print("No Spotify match found :(")

