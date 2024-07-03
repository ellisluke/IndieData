### USER INITIALIZATION ###
InstagramHandle = "aftersixmusic" # Replace with username of Instagram profile
YoutubeLink = "https://www.youtube.com/@AfterSixMusic" # Replace with the link to your YouTube Channel
SpotifyLink = "https://open.spotify.com/artist/4ujBf6QyfvJB2RXCepYrXW" # Replace with the link to your Spotify Artist page

# IMPORTS

import requests
import instaloader
from bs4 import BeautifulSoup
import re

# GET DATA FROM LINKS

# Instagram Profile data using instagramy
# L = instaloader.Instaloader()
# IGProfile = instaloader.Profile.from_username(L.context, "lukegrooves") # https://instaloader.github.io/module/structures.html#instaloader.Profile.followers
# currentIGFollowers = IGProfile.followers

# # Youtube Channel data using 
# youtubeGet = requests.get(YoutubeLink)
# youtubeSoup = BeautifulSoup(youtubeGet.text, 'html.parser')

# Purpose is to whittle down the results and only search this tag for subscriber count
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
# print(youtubeGet)
# targetScriptTag = str(find_nth_tag(youtubeSoup, "script", 36))

# ytRePattern = '"content":"(\d+) subscribers"'
# ytMatches = re.findall(ytRePattern, targetScriptTag)

# if ytMatches:
#     currentSubscribers = int(ytMatches[0])
#     print(currentSubscribers)
# else:
#     print("No YouTube match found :(")


# Spotify Artist data using BeautifulSoup web scraping

spotifyGet = requests.get(SpotifyLink)
spotifySoup = BeautifulSoup(spotifyGet.text, 'html.parser')
targetMetaTag = str(find_nth_tag(spotifySoup, "meta", 6))
spotifyRePattern = '(\d+) monthly listeners.'
spotifyMatches = re.findall(spotifyRePattern, targetMetaTag)

if spotifyMatches:
    currentMonthlyListeners = int(spotifyMatches[0])
    print(currentMonthlyListeners)
else: 
    print("No Spotify match found :(")

