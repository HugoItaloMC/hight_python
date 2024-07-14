from pathlib import Path
from typing import Generator, Optional
from multiprocessing import RLock, Queue

import sqlalchemy as sa
from sqlalchemy.future.engine import Engine

from app.utils.core.singleton import Singleton


class Handler(metaclass=Singleton):

    def __getattr__(self, attr):
        valur = attr
        setattr(attr, self, valur)
        return valur


class HandlerWrapper(Handler):

    def __init__(self, args) -> None:
        self._args = args
        self.queue = Queue()

    def _container(self, args):

        """

        :param args: Outras Coroutinas/Métodos
        :return: None
        """
        self.queue.put(args)
        create_ = self._coroutine()

        # Juntos yield e send dão uma maneira padrão ao generator function de variar em resposta a um estímulo externo

        next(create_)  # Inicia o generator function
        with self._lock:
            create_.send(self.queue.get())

    def _coroutine(self) -> Generator:
        """
        :return: generator function
        """
        while True:
            yield


class HandlerORM(Handler):

    def __init__(self):
        self._URLBD = "postgresql://postgres:Acesso93#@localhost:5432"
        self._engine: Optional[Engine] = None

    def create_engine(self, sqlite: bool = None):
        if self._engine:
            return

        if sqlite:
            file_db = 'db/db.app.sqlite'
            path_Db = Path(file_db).parent
            path_Db.mkdir(parents=True,
                          exist_ok=True)

            # Criando  engine sqlite
            self._engine = sa.create_engine(url=f'sqlite:///{file_db}', echo=False, connect_args={"check_same_threads": False})

        else: # Definicões PostgreSql
            self._engine = sa.create_engine(url=self._URLBD, echo=False, pool_size=100, max_overflow=200, pool_timeout=1000)
        return self._engine

    def create_tables(self) -> None:

        if not self._engine:
            self.create_engine()

        import app.db.__all_models
        from app.utils.base_model import Base
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
