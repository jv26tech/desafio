import abc

from desafio_crud.config import Config
from desafio_crud.db import DBBase, DBManager
from desafio_crud.models import BaseModel, PostModel, UserModel
from desafio_crud.schemas import PostSchema
from desafio_crud.services.post import PostService
from desafio_crud.services.user import UserService


class ScriptInterface(abc.ABC):
    def __init__(self, db: DBBase) -> None:
        self.db = db
        self.run()

    @abc.abstractmethod
    def run(): ...


class ScriptSetupDB(ScriptInterface):
    def __init__(self, db: DBManager, tables: list[BaseModel]):
        self.tables = tables
        super().__init__(db)

    def run(self):
        self.db.create_tables(self.tables)
        self.db.clear_tables()


class ScriptFillTables(ScriptInterface):
    def run(self):
        self.posts(5)
        self.users(5)

    def posts(self, qtd: int):
        ps = PostService(Config)
        posts = ps.listar()
        for post in posts[:qtd]:
            post_obj = PostModel(**post)
            post_id = self.db.create(post_obj)
            print(f"Post {post['title']} no DB com ID: {post_id}")

    def users(self, qtd: int):
        us = UserService(Config)
        users = us.listar()
        for user in users[:qtd]:
            user_obj = UserModel(**user)
            user_id = self.db.create(user_obj)
            print(f"User {user['username']} no DB com ID: {user_id}")


class ScriptPost(ScriptInterface):
    def run(self):
        ps = PostService(Config)
        novo_post = PostSchema('Título de Teste', 'Corpo de Teste', 1)
        res_post = ps.criar(novo_post)
        if res_post:
            post = PostModel(**res_post)
            post_id = self.db.create(post)
            print(f'Novo post inserido com ID: {post_id}')

            atual_post = PostSchema(
                'Titulo Atualizado', 'Corpo Atualizado', 2, 1
            )
            atual_res = ps.modificar(atual_post)
            if atual_res:
                print(f'Post de id {post_id} modificado.')

                post = PostModel(**atual_res)
                self.db.update(post, post_id)
                print(f'Post de id {post_id} atualizado no banco.')

            post = ps.remover(post_id)
            print(f'Post removido {post}')
            post_id = self.db.delete(PostModel, post_id)
            print(f'Post removido do banco com ID: {post_id}')


class ScriptUser(ScriptInterface):
    def run(self):
        us = UserService(Config)
        users = us.listar()
        for user in users[5:]:
            usr = UserModel(**user)
            post_id = self.db.create(usr)
            print(f"User {user['username']} inserido com ID: {post_id}")
