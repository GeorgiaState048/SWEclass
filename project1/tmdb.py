import os
import requests
from dotenv import load_dotenv, find_dotenv

# will probably be using this to find movie information:
# https://developers.themoviedb.org/3/find/find-by-id

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + os.getenv("TMDB_KEY")

def get_movie_data():
    """returns info about a movie"""

    query_params = {

    }

    response = requests.get(BASE_URL, params=query_params)
    response_json = response.json()
    results = response_json['results']

    return results[0]['original_title']
