import requests
from bs4 import BeautifulSoup
import datetime
url = "https://www.pixelford.com/blog"

response = requests.get(
    url,
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    },
)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# a_tag = soup.find_all('a', class_="entry-title-link")
# res = list(map(lambda x:x.get_text(), a_tag))
# print(res)
# [print(a.get_text()) for a in a_tag]

blogs = soup.find_all("article", class_='type-post')

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
    time_str = blog.find('time', class_="entry-time").get('datetime')
    time = datetime.datetime.fromisoformat(time_str)
    pretty_time = time.strftime("%b %d %Y")
    print(f"{pretty_time} - {title}")