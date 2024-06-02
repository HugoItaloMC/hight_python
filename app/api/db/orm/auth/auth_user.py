from sqlalchemy import select

from orm.models.user import User

from orm.utils.db_session import create_session
from werkzeug.security import generate_password_hash, check_password_hash


async def post_user(**kw) -> User:
    name = kw['name']
    passwd = kw['passwd']

    _user: User = User(name=name, passwd=generate_password_hash(passwd))
    async with create_session() as handler, handler.begin():
        handler.add(_user)
        return _user


async def get_user(**kw):
    name = kw['name']
    passwd = kw['passwd']

    async with create_session() as handler, handler.begin():
        _user: User = await handler.scalar(select(User).where(User.name == name and check_password_hash(User.passwd, passwd)))
        print(_user)
