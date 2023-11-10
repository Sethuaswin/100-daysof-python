#########################################################
# This file is used for web scraping using beautiful soup
#########################################################

from bs4 import BeautifulSoup

with open("Day 45 - Web Scraping/website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get('class'))

# selector method is CSS selector
company_url = soup.select_one(selector='p a')
# print(company_url)

name = soup.select_one(selector='#name')
# print(name)

headings = soup.select(".heading")
print(headings)

