
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()  # how set class work


def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        # print(urls)

        for duplicate_url in urls:
            if duplicate_url not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, duplicate_url)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
                else:
                    pass


url = input("Enter the url you want to scrappe: ")
keyword = input("Enter the keyword to search for in the url provided: ")
spider_urls(url, keyword)
