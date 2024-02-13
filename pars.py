from bs4 import BeautifulSoup
import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"}
def get_info():
    for count in range(0, 5, 1):
        url = f'https://manufacturers.ru/companies?type=4577&page={count}'
        pages = requests.get(url, headers=headers)
        soup = BeautifulSoup(pages.text, 'html.parser')
        data = soup.find_all('div', class_='sim-title')
        for i in data:
            card_url = "https://manufacturers.ru" + i.find('a').get('href')
            yield card_url

def array():
    for cards in get_info():
        pages = requests.get(cards, headers=headers)
        soup = BeautifulSoup(pages.text, 'html.parser')
        # Наименование компании
        name = soup.find('h1', class_='like-h1').text
        # Почты
        email = soup.find('a', {"href": re.compile(r'''(
        [a-zA-Z0-9._%+-] + #username
        @                   # @symbole
        [a-zA-Z0-9.-] +     # domain
        (\.[a-zA-Z]{2,4})   # dot-something
        )''', re.VERBOSE)})
        # О компании
        about1 = soup.find('div', id='about')
        about = about1.find('p').text
        if email is not None:
            email = email.text
            yield name, email, about