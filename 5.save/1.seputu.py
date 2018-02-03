import requests
from bs4 import BeautifulSoup
import json

parser_url = "http://seputu.com"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"

headers = {"User_Agent":user_agent}

html_content = requests.get(parser_url, headers=headers)

#print(html_content.text)
soup = BeautifulSoup(html_content.text, "lxml", from_encoding="utf-8")
content = []
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find("h2")
    #print(h2)
    if h2 != None:
        h2_title = h2.string
        section_list = []
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            #print(href, box_title)
            section_list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content': section_list})

with open("daomu.json", "w") as fw:
    json.dump(content, fp=fw, indent=4)
