import requests
import time

from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    HEADER = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, header=HEADER, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css("div.meta-category span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    link_next_page = "https://blog.betrybe.com"

    links_list = []
    news = []

    while len(links_list) < amount:
        page_html = fetch(link_next_page)
        links_list.extend(scrape_updates(page_html))
        link_next_page = scrape_next_page_link(page_html)

    for link in links_list[:amount]:
        news.append(scrape_news(fetch(link)))

    create_news(news)
    return news
