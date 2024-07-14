from multiprocessing import RLock
import os

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from flask import session

from sqlalchemy import insert
from app.src.db_session import DBSession
from app.db.models.auth import User


class RepoUser:

    def __init__(self, **kw):
        self.name = kw['name']
        self.passwd = kw['passwd']
        self.email = kw['email']
        self.db = DBSession()
        self._lock = RLock()

    def __iter__(self, **kw):

        with self._lock:
            db = self.db()
            user_ = insert(User).values(name=self.name,
                                        passwd=self.passwd,
                                        email=self.email).returning(User.id)
            user_stmt = db.execute(user_)
            user_id = user_stmt.scalar()
            db.commit()
            db.close()
            return user_id

    def __call__(self, *args, **kwargs):
        return self.__iter__()


class RepoUserLogin:

    def __init__(self, **kw):
        self.name = kw['name']
        self.passwd = kw['passwd']
        self.email = kw['email']
        self.db = DBSession()
        self._lock = RLock()
        self.token = None

    def __iter__(self, **kw):
        with self._lock:
            error = None
            db = self.db()
            user_: User = db.query(User).filter(User.name == self.name, User.email == self.email).one()

            if user_ is None:
                error = 'Incorrect Email and Name'
                return error
            elif not check_password_hash(user_.passwd, self.passwd):
                error = 'Incorrect Passwd'
                return error
            if error is None and user_ and check_password_hash(user_.passwd, self.passwd):
                self.token = create_access_token(identity=user_.id)

                session.clear()
                session['user_id'] = user_.id
                return user_

    def __call__(self, *args, **kwargs):
        return self.__iter__()


class RepoUserID:

    def __init__(self, **kw):
        self.id = kw['id']
        self.db = DBSession()

    def __call__(self, *args, **kwargs):
        db = self.db()
        user: User = db.query(User).filter(User.id == self.id).one()
        return user.id

