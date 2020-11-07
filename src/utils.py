import requests
from bs4 import BeautifulSoup

def get_course(key_word):
    res = requests.get(f"https://es.coursera.org/search?query={key_word}")
    soup = BeautifulSoup(res.text)

    data = {
        "images": [img['src'] for img in soup.find('div', {'class': 'tab-contents'}).find_all('img')],
        "titles": [e.text for e in soup.find_all('h2', {"class": "card-title"})],
        "partners": [e.text for e in soup.find_all('span', {"class": "partner-name m-b-1s"})],
        "ratings": [e.text for e in soup.find_all('span', {"class": "ratings-text"})],
        "ratings_counts": [e.text for e in soup.find_all('span', {"class": "ratings-count"})],
        "students": [e.text for e in soup.find_all('span', {"class": "enrollment-number"})]
    }
    return data
    