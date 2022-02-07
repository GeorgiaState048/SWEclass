import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
NYT_KEY = "wBIUbEzYfCbgW3yh5Wo85Kdrxi5JGOPf"

query_params = {
    #"api-key": NYT_KEY,
    "api-key": os.getenv("NYT_KEY"),
    "q": "trees", # q = query = search = search articles with keyword "tree"
    "page":(0,1)
}

response = requests.get(BASE_URL, params=query_params)

"""NY Times articles is essentially a list of dictionaries. Each section has a subsection of other dictionaries and so on
You must call each section to access the subsections unitl you get the info you need"""
# print(response.json())
# print(response.json()["copyright"])
# print(response.json()["response"]["docs"][0]["headline"]["main"]) 
response_json = response.json()
#print(json.dumps(response_json, indent=4, sort_keys=True))
print(response_json)
# docs = response_json["response"]["docs"]
# count = 1
# for doc in docs:
#    print(count, " ", doc["headline"]["main"], " ", doc["web_url"])
#    count += 1
