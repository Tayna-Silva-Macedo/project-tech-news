from tech_news.database import search_news


def create_tuple_list(news_list):
    tuple_list = [(news["title"], news["url"]) for news in news_list]
    return tuple_list


# Requisito 7
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return create_tuple_list(news_list)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
