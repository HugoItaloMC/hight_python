from pathlib import Path
from typing import Generator, Optional
from multiprocessing import RLock
from queue import Queue
from functools import wrap

import sqlalchemy as sa
from sqlalchemy.future.engine import Engine

from app.src.core.singleton import Singleton


class Handler(metaclass=Singleton):

    def __getattr__(self, attr):
        valur = attr
        setattr(self, attr, valur)
        return valur


class HandlerWrapper(Handler):

    def __init__(self) -> None:
        self.queue = Queue()
        self._lock = RLock()

    def _container(self, args, **kw):
        """

        :param args: Outras Coroutinas/Métodos
        :return: None
        """

        with self._lock:
            self.queue.put(self._coroutine())

            # Juntos yield e send dão uma maneira padrão ao generator function de variar em resposta a um estímulo externo
            self.queue.put(next(self.queue.get().task_done()))  # Inicia o generator function

            for _ in range(1, kw['cores'], 1):
                self.queue.put(args)

                coroutine = self.queue.get().task_done()  # Indicando que após `.get()` a chamada foi finalizada
                arg = self.queue.get().task_done()  # Outro objeto

                coroutine.send(arg)  # Enviando outro objeto como generator

    def _coroutine(self) -> Generator:
        """
        :return: generator function
        """
        while True:
            yield


class HandlerORM(Handler):

    def __init__(self):
        super(__class__, self).__init__()
        self._URLBD = "postgresql://italo:d310e5ebcaf3@localhost:5432/app2manager"
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
        from app.src.base_model import Base
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
