import urllib3
from bs4 import BeautifulSoup

year = input("which year do you want to watch? ")
url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"

finalUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(finalUrl, "lxml")

movies = soup.findAll('h3', attrs={'class': 'lister-item-header'})

print("top 50 movies in " + year + ": ")
for movie in movies:
    name = movie.text.replace("\n", " ")
    print(name)
