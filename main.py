import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Grab all <h3 class="title"> elements
movie_tags = soup.find_all("h3", class_="title")


with open("movies.txt", "a", encoding="utf-8") as data_file:
    for tag in movie_tags:
        movie_name = tag.getText()
        data_file.write(movie_name + '\n')