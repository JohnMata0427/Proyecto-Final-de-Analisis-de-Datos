import requests
from bs4 import BeautifulSoup
import csv

url_base = "https://concertful.com/top?page="
num_pages = 1
concerts_data = []

def get_concerts(url, num_pages):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    concerts_list = soup.find_all("td", class_="alt")
    
    for concert in concerts_list:
        name = concert.find("a").getText().strip()
        abbr = concert.find_all("abbr")
        concerts_and_date = abbr[0].getText().split(" to ")
        num_of_concerts = concerts_and_date[0].strip()
        try:
            date = concerts_and_date[1].strip()
        except Exception:
            date = None
        genres = abbr[1].getText().strip()

        concerts_data.append({
            "id": len(concerts_data) + 1,
            "name": name,
            "num_of_concerts": num_of_concerts,
            "date": date,
            "genres": genres
        })
    
    num_pages += 1
    if num_pages < 41:
        print(f"Getting concerts from page {num_pages}...")
        get_concerts(f"https://concertful.com/top?page={num_pages}", num_pages)

get_concerts(url_base + str(num_pages), num_pages)

print(concerts_data)

with open("concerts-artists.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "num_of_concerts", "date", "genres"])
    for concert in concerts_data:
        writer.writerow([concert['name'], concert['num_of_concerts'], concert['date'], concert['genres']])