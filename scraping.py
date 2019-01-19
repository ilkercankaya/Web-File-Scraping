from bs4 import BeautifulSoup
import requests
import csv

# Manage CSV file, Writer

csv_file = open("corey.csv", 'w')
csv_file_index = open("index.csv", 'w')

# Corey writer
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

csv_writer_index = csv.writer(csv_file_index)
csv_writer_index.writerow(['Headline', 'Summary', "Links"])

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
match = soup.find_all('div', class_='article')
# See the ref of all pages in article
for article in match:
    headline = article.h2.text
    summary = article.p.text
    link = article.h2.a["href"]

    # Append to CSV file
    csv_writer_index.writerow([headline, summary, link])

# Scapes coreyms.com
URL = "http://coreyms.com/"
# Text gets the HTML text
source = requests.get(URL).text
soup_corey = BeautifulSoup(source, 'lxml')

# See the page
# print(soup_corey.prettify())

# Find the first articles
article_first = soup_corey.find('article')
# print(article_first.prettify())
# summary = article_first.find('div', class_="entry-content").p.text
# print(summary)

# Get the youtube link
vid_source = article_first.find('iframe', class_="youtube-player")['src']
# print(vid_source)

vid_id = vid_source.split('/')[4]
# print(vid_id)

vid_id = vid_id.split('?')[0]
# print(vid_id)

# F is available over python 3.6
yt_link = f"https://www.youtube.com/watch?v={vid_id}"
# print(yt_link)

articles = soup_corey.find_all('article')
# print(len(articles))
for article in articles:
    try:
        # Get parapgraph
        headline = article.h2.a.text
        summary = article.find('div', class_="entry-content").p.text
        # Get the youtube link
        vid_source = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid_source.split('/')[4]
        vid_id = vid_id.split('?')[0]

        # F is available over python 3.6
        yt_link = f"https://www.youtube.com/watch?v={vid_id}"
    except (AttributeError, KeyError) as ex:
        pass
        # or make the information None: yt_link = None

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
print("Finished Scraping both file and website!")