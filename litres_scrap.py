# --------------------подключение библ---------------
from bs4 import BeautifulSoup
import requests
from requests import get
import csv
from transliterate import translit
# ----------------------------------------------------
books = []
list = []
url = 'https://www.litres.ru/pages/rmd_search/?q=' 
inputSearch = inputSearch = input('Введите запрос: ')
# создание строки запроса
l = inputSearch.split()
req = '+'.join(l) 
url = url + req
print(url) # вывод итогового запроса
# запрос
response = get(url)
html_soup = BeautifulSoup(response.text, "html.parser")
# получение необходимого блока с информацией для скрапинга
div_data = html_soup.find_all('div', class_='art-item search__item item__type_art')
# проверка на наличие блоков на странице
if div_data != []:
    books.extend(div_data)
count = 0
# скрапинг названия, автора и ссылки на книгу
while count < len(books):
    info = books[int(count)]
    titleBook = translit(info.find('a',{"class":"art-item__name__href"}).text , language_code='ru', reversed=True)
    author = translit(info.find('a',{"class":"art-item__author_label rmd-author-href"}).text, language_code='ru', reversed=True)
    src = info.find('a',{"class":"art-item__name__href"})['href']
    list.append([titleBook, author, 'https://www.litres.ru' + src])
    count+=1
# сохранине в файл
for data in list:
    with open ("data.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow(data)
