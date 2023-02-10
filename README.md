# Bem-vindo ao Projeto Tech News!

Este é um projeto da [Trybe](https://www.betrybe.com/) que foi desenvolvido no módulo de Ciência da Computação.

Trata-se de uma aplicação que realiza uma raspagem no [Blog da Trybe](https://blog.betrybe.com/), salva as notícias em um banco de dados e permite realizar consultas pelo título da notícia, data de sua publicação ou qual a sua categoria, além disso é possível listar quais são as categorias que aparecem com maior frequência.

## Tecnologias utilizadas

Em seu desenvolvimento foi utilizada linguagem ***Python*** para escrever os códigos, biblioteca ***Requests*** para realizar as requisições HTTP, ***Parsel*** extrair os dados do conteúdo HTML e, por fim, biblioteca ***PyMongo*** para salvar as notícias no banco de dados ***MongoDB***.

Fora isso, foi utilizado o framework ***pytest***, para testar uma função que já havia sido implementada pela Trybe.

## Habilidades que foram trabalhadas:

  - Aplicação de técnicas de raspagem de dados; 
  - Extração de dados de conteúdo HTML;
  - Armazenamento dos dados obtidos em um banco de dados.

## Como rodar o projeto na sua máquina:

1. Navegue até o local onde deseja clonar o repositório e utilize o **git clone**:
```
git clone git@github.com:Tayna-Silva-Macedo/project-inventory-report.git
```

2. Acesse o diretório do projeto **
project-inventory-report**:
```
cd project-inventory-report
```

3. Crie e ative um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Instale o próprio projeto:
```
pip install .
```

6. Execute o projeto utilizando o comando:
```
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```
> ℹ️ O tipo de relatório deve ser "simples" ou "completo".

Exemplo: ```inventory_report inventory_report/data/inventory.csv simples```

7. Para rodar os testes é utilizado o seguinte comando:

```
python3 -m pytest
```
