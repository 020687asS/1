import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_user_rates(user_login):
    data = []

    #while True:
    url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'lxml')
    # Находим все элементы <div> с классом item и классом item even
    entries = soup.find_all('div', class_=['item','item even'])
        #if len(entries) == 0:
            #break
    for entry in entries:
        film_name = entry.find('div', class_='nameRus')
        name = film_name.find('a').text
        film_rating = entry.find('div', class_='rating')
        rating = film_rating.find().text
        vote = entry.find('div', class_='vote').text
        data.append({'film name': name, 'film rating': rating, 'user rating': vote})

    return data


user_rates = collect_user_rates(user_login = '140875992')
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')
