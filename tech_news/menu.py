import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    option_selected = input(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n "
        "5 - Sair.\n "
    )

    if option_selected == "0":
        amount = input("Digite quantas notícias serão buscadas: ")
        return get_tech_news(amount)
    elif option_selected == "1":
        title = input("Digite o título: ")
        return search_by_title(title)
    elif option_selected == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
        return search_by_date(date)
    elif option_selected == "3":
        category = input("Digite a categoria: ")
        return search_by_category(category)
    elif option_selected == "4":
        return top_5_categories()
    elif option_selected == "5":
        return print("Encerrando script")
    else:
        return sys.stderr.write("Opção inválida\n")
