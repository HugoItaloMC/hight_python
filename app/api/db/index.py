from orm.utils.db_session import create_tables
from orm.auth.auth_user import post_user, get_user
from orm.wrapper import coroutine


def init_db():
    coroutine(args=create_tables())


def register_user(name: str, passwd: str):
    coroutine(args=post_user(name=name, passwd=passwd))


def login_user(name: str, passwd: str):
    coroutine(args=get_user(name=name, passwd=passwd))


if __name__ == '__main__':
    # init_db()
    # register_user(name='Italo', passwd='TesteSenha')
    login_user(name='Italo', passwd='TesteSenha')
