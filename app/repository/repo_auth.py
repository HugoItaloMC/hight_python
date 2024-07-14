from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import insert, select
from app.utils.db_session import create_session
from app.db.models.user import User


def register_user(**kw):
    name = kw['name']
    passwd = kw['passwd']
    email = kw['email']

    with create_session() as handler, handler.begin():

        user_ = insert(User).values(name=name, passwd=generate_password_hash(passwd), email=email).returning(User.id)
        user_stmt = handler.execute(user_)
        user_id = user_stmt.scalar()
        return user_id


def login_user(**kw):

    name = kw['name']
    email = kw['email']
    passwd = kw['passwd']


