# imdb top 250 film name and raiting
import requests
from bs4 import BeautifulSoup

imdb_url = "https://www.imdb.com/chart/top/"

result = requests.get(imdb_url)
soup = BeautifulSoup(result.content, "html.parser")

all_films = soup.find_all("table",{'class':'chart full-width'})

film_table = (all_films[0].contents)[len(all_films[0].contents)-2]
film_table = film_table.find_all("tr")

for film in film_table:
    # Film Name Table 
    film_title = film.find_all("td",{'class':'titleColumn'})
    # Film Raitings Table
    film_raitings = film.find_all("td",{'class':'ratingColumn imdbRating'})

    # Film Names
    film_name = film_title[0].text
    film_name = film_name.replace("\n","")

    # Film Raitings
    film_raitings_point = film_raitings[0].text
    film_raitings_point = film_raitings_point.replace("\n","")

    # Film names and raitings
    to_connect = (film_name) + (" ⭐"+film_raitings_point)

    print(to_connect)
