class BaseModel:
    """
    Base model for database tables.
    """

    tablename: str = ''
    table: str = ''
    id: int
    data: dict = {}

    def table_setup(self) -> str:
        """
        Returns table creation string
        """
        return self.table

    def get_data(self) -> str:
        return self.data


class PostModel(BaseModel):
    """
    Representacao da tabela 'posts' no banco de dados.
    """

    tablename = 'posts'

    table = """
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                user_id INT,
                title VARCHAR(255),
                body TEXT
            );
            """

    def __init__(self, userId, title, body, *args, **kwargs):
        self.data = {'user_id': userId, 'title': title, 'body': body}


class UserModel(BaseModel):
    """
    Representacao da tabela 'users' no banco de dados.
    """

    tablename = 'users'

    table = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                username VARCHAR(255),
                email VARCHAR(255),
                phone VARCHAR(255),
                website VARCHAR(255)
            );
            """

    def __init__(self, name, username, email, phone, website, *args, **kwargs):
        self.data = {
            'name': name,
            'username': username,
            'email': email,
            'phone': phone,
            'website': website,
        }
