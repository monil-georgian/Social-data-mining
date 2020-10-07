import requests
import pymongo
from pymongo import MongoClient
import sys, json

#skip_num is used for skipping fetched results, as an alternative to pagination
skip_num = 0
    
while True:
    url = ("https://api.boardgameatlas.com/api/search?skip=" + str(skip_num))
        
    parameters = {"order_by": "popularity", "limit": 100, "skip": skip_num, "gt_price": 0.1, "client_id": "ieVACdbciW"}
        
    response = requests.get(url, params=parameters)
        
    # Get the response data as a python object. Verify that it's a dictionary.
    data = response.json()
    
    games = data["games"]
   
    client = pymongo.MongoClient("mongodb+srv://boardgames:boardgames@social-data-mining.ashep.azure.mongodb.net/boardgames?retryWrites=true&w=majority")
    db = client.boardgames
    BoardGames = db.boardgames
        
    BoardGames.insert_many(games)
    
    skip_num = skip_num + 100
        
    if skip_num > 100:
        break
    
print ("Database populated from the API")
