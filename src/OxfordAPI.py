import requests
import json

appID = '3d38b8f3'
appKey = '01bfb57f8c199295f24344c7c8e70e9e'

language = 'en'
rawURL = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections'

def lemmatronCheck(wordID):
    url = rawURL + '/' + language + '/' + wordID.lower()
    r = requests.get(url, headers = {'app_id': appID, 'app_key': appKey})
    return r
