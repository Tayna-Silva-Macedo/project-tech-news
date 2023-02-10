import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


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

    responses_input = {
        "0": {
            "message": "Digite quantas notícias serão buscadas: ",
            "type": int,
            "func": get_tech_news,
        },
        "1": {
            "message": "Digite o título: ",
            "type": str,
            "func": search_by_title,
        },
        "2": {
            "message": "Digite a data no formato aaaa-mm-dd: ",
            "type": str,
            "func": search_by_date,
        },
        "3": {
            "message": "Digite a categoria: ",
            "type": str,
            "func": search_by_category,
        },
    }

    responses = {"4": {"func": top_5_categories}}

    if option_selected in responses_input.keys():
        user_input = input(responses_input[option_selected]["message"])
        return responses_input[option_selected]["func"](
            responses_input[option_selected]["type"](user_input)
        )
    elif option_selected in responses.keys():
        return responses[option_selected]["func"]()
    elif option_selected == "5":
        return print("Encerrando script")
    else:
        return sys.stderr.write("Opção inválida\n")
