from http import HTTPStatus

import requests
from config import Config
from schemas import PostSchema


class PostService:
    """
    CRUD para interagir com o endpoint '/posts'
    """

    def __init__(self, config: Config):
        self.BASE_URL = config.BASE_URL

    def criar(self, data: PostSchema) -> dict:
        payload = {
            'title': data.title,
            'body': data.body,
            'userId': data.userId,
        }
        response = requests.post(f'{self.BASE_URL}/posts', json=payload)
        if response.status_code == HTTPStatus.CREATED:
            return response.json()
        else:
            return None

    def retornar(self, id) -> dict:
        response = requests.get(f'{self.BASE_URL}/posts{id}')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    def listar(self) -> list:
        response = requests.get(f'{self.BASE_URL}/posts')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return []

    def modificar(self, data: PostSchema) -> dict:
        payload = {
            'title': data.title,
            'body': data.body,
            'userId': data.userId,
        }
        response = requests.put(
            f'{self.BASE_URL}/posts/{data.id}', json=payload
        )
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    def remover(self, id) -> dict:
        response = requests.delete(f'{self.BASE_URL}/posts/{id}')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None
