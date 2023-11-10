#########################################################
# This file is used for web scraping using beautiful soup
#########################################################

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name='a', rel="noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Index of largest upvote score
largets_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largets_index])
print(article_links[largets_index])
print(article_upvotes[largets_index])



