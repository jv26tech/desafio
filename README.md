# Python Web API

## Requisitos (execucao por venv)
- Python 3.10 ou superior
- PostgreSQL

## Requisitos (execucao por Docker)
- Docker
- docker-compose

## Requisitos (execucao por poetry)
- Poetry

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/jv26tech/teste
    cd teste
    ```

## venv

1. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

2. Execute o ambiente virtual (*Linux*):
    ```bash
    source venv/bin/activate
    ```

3. Execute o ambiente virtual (*Windows*):
     ```bash
    ./venv/Scripts/activate.bat
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Poetry

1. Instale as dependencias:
    ```bash
    poetry install
    ```

2. Execute o shell:
    ```bash
    poetry shell
    ```

## Banco de dados
1. Configure o banco de dados PostgreSQL:
    - (local) Crie um banco de dados e atualize as informações de conexão no arquivo `.env`.
    - (docker) execute o comando:

    ```bash
    docker-compose up
    ```

## Execução

1. (venv) Execute o script para criar as tabelas e rodar comandos CRUD:
    ```bash
    python desafio_crud/main.py
    ```

1. (Poetry) Execute o script para criar as tabelas e rodar comandos CRUD:
    ```bash
    python desafio_crud/main.py
    ```

2. (*opcional*)Execute os testes:
    ```bash
    task test
    ```

## Autor
Joao Victor Ferrer Morgado