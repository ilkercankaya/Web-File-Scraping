from bs4 import BeautifulSoup
import requests

# Scapes index.html
with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# See the page
# print(soup.prettify())

# Gets the first title
# print(soup.title.text)

# Gets the first div
# print(soup.div)

# Gets the footer
# match = soup.find('div', class_='footer')
# print(match)

# Gets all the divs that are article class
# match = soup.find_all('div', class_='article')
# See the ref of all pages in article
# for article in match:
#     print(article.h2.a["href"])







