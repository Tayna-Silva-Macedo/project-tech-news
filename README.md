# Bem-vindo ao Projeto Tech News!

Este é um projeto da [Trybe](https://www.betrybe.com/) que foi desenvolvido no módulo de Ciência da Computação.

Trata-se de uma aplicação que realiza uma raspagem de dados no [Blog da Trybe](https://blog.betrybe.com/), salva as notícias em um banco de dados e permite realizar consultas pelo título da notícia, data de sua publicação ou qual a sua categoria, além disso, é possível listar quais são as cinco categorias que aparecem com maior frequência.

## Tecnologias utilizadas

Em seu desenvolvimento foi utilizada linguagem ***Python*** para escrever os códigos, biblioteca ***Requests*** para realizar as requisições HTTP, ***Parsel*** para extrair os dados do conteúdo HTML e, por fim, biblioteca ***PyMongo*** para salvar as notícias no banco de dados ***MongoDB***.

Fora isso, foi utilizado o framework ***pytest***, para testar um método que já havia sido implementado pela Trybe.

## Habilidades que foram trabalhadas:

  - Aplicação de técnicas de raspagem de dados; 
  - Extração de dados de conteúdo HTML;
  - Armazenamento dos dados obtidos em um banco de dados;
  - Testagem de método fazendo mock do retorno do banco de dados. 

## Como rodar o projeto na sua máquina:

1. Navegue até o local onde deseja clonar o repositório e utilize o **git clone**:
```
git clone git@github.com:Tayna-Silva-Macedo/project-tech-news.git
```

2. Acesse o diretório do projeto **project-tech-news**:
```
cd project-tech-news
```

3. Crie e ative um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Rode o MongoDB via docker:
```
docker-compose up -d mongodb
```

6. Execute o projeto e selecione a opção que deseja de acordo com as opções apresentadas no menu:
```
tech-news-analyzer
```
> ℹ️ Caso seja a primeira vez utilizando a aplicação, é importante que o banco seja populado antes, para isso, selecione a opção 0, quando solicitado. 


7. Para rodar os testes é utilizado o seguinte comando:
```
python3 -m pytest
```
