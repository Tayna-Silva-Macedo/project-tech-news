import sys


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
    elif option_selected == "1":
        title = input("Digite o título: ")
    elif option_selected == "2":
        date = input("Digite a data no formato aaaa-mm-dd: ")
    elif option_selected == "3":
        category = input("Digite a categoria: ")
    else:
        return print("Opção inválida", file=sys.stderr)
