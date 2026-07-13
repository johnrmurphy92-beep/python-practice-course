#Import relevant libraries
import requests
import sys
import json

#Check for errors
if len(sys.argv) != 2:
    sys.exit("Invalid input")

#Execute API request
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

itunes = response.json()
for result in itunes["results"]:
    print(result["trackName"])