# importing BeautifulSoup and requests module for parsing
from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# Getting the response for top 100 movies
response = requests.get(URL)
top_100_movie_page = response.text 

# Intializing BeautifulSoup with the top_100_movie_page html text
soup = BeautifulSoup(top_100_movie_page, "html.parser")

# Getting the 100 movies elements
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

# Getting the movies name list and reverse the list for the ascending order
top_100_movies = [movie.getText() for movie in movies][::-1]

# Creating top_100_movies_to_watch.txt file
with open("Day 45 - Web Scraping/100-movies-to-watch/top_100_movies_to_watch.txt", "w") as f:
    f.write("\n".join(str(movie) for movie in top_100_movies))