from datetime import datetime

from tech_news.database import search_news


def create_tuple_list(news_list):
    return [(news["title"], news["url"]) for news in news_list]


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return create_tuple_list(news_list)


def search_by_date(date):
    try:
        formated_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": {"$regex": formated_date}})
    return create_tuple_list(news_list)


def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return create_tuple_list(news_list)
