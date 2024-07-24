from http import HTTPStatus

import requests

from desafio_crud.config import Config
from desafio_crud.schemas import UserSchema


class UserService:
    """
    CRUD para interagir com o endpoint '/users'
    """

    def __init__(self, config: Config):
        self.BASE_URL = config.BASE_URL

    def criar(self, data: UserSchema):
        payload = {
            'name': data.name,
            'username': data.username,
            'email': data.email,
            'phone': data.phone,
            'website': data.website,
        }
        response = requests.post(f'{self.BASE_URL}/users', json=payload)
        if response.status_code == HTTPStatus.CREATED:
            return response.json()
        else:
            return None

    def retornar(self, id) -> dict:
        response = requests.get(f'{self.BASE_URL}/users/{id}')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    def listar(self):
        response = requests.get(f'{self.BASE_URL}/users')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return []

    def modificar(self, data: UserSchema):
        payload = {
            'name': data.name,
            'username': data.username,
            'email': data.email,
            'phone': data.phone,
            'website': data.website,
        }
        response = requests.patch(
            f'{self.BASE_URL}/users/{data.id}', json=payload
        )
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    def remover(self, id):
        response = requests.delete(f'{self.BASE_URL}/users/{id}')
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None
