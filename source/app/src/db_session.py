from sqlalchemy.orm import sessionmaker, Session

from app.src.core.handlers import HandlerORM


class DBSession(HandlerORM):

    def __init__(self):
        super(__class__, self).__init__()

    def __iter__(self):

        if not self._engine:
            # To `sqlite` db add parameter `sqlite=True`
            self.create_engine()

        __session = sessionmaker(self._engine, expire_on_commit=False, class_=Session)
        session = __session()
        return session

    def __call__(self, *args, **kwargs):
        return self.__iter__()


class DBInit(HandlerORM):

    def __init__(self):
        super(__class__, self).__init__()

    def __iter__(self):
        return self.create_tables()

    def __call__(self):
        return self.__iter__()
