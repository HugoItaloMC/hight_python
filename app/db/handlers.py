from typing import Optional
from pathlib import Path

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy.engine import Engine

__all__ = ['HandlerORM', 'Base']


class Base(DeclarativeBase):
    ...


class Singleton(type):
    # Create type for instance control

    def __new__(meta, *args, **kwargs):
        # Behaviour to entailsen in childer object
        return type.__new__(meta, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # Lonely instance
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class HandlerORM(metaclass=Singleton):
    
    
    def __init__(self):
        self.__db_url: str = 'postgresql+psycopg2://auth:1cdc09ad55da@localhost:5433/auth'
        self._engine: Optional[Engine] = None
        self.sqlite: Optional[bool] = False
        self.__session: Session = None 


    def __iter__(self):
        """
          - Sempre que tiver um 'yield' na funcão, a mesma vai aguardar a chamada do método next()
          para iniciar a coroutina, após a mesma iniciada controlados sinais externos com o méto-
          do send() que faz um contrato externo podendo aplicar lógica condicional e aplicar des-
          vios de comportamentos no objeto.
        """
        
        # Aguardando next()
        send = yield
        
        # Verificando send()
        if 'SET' in send:  
            print('send(SET)')
            self()
            yield next(self)

    def __call__(self):
        self.sqlite = True

        if self._engine:
            return self
        
        if self.sqlite:
            path = Path('app.db').parent
            path.mkdir(parents=True, exist_ok=True)

            self._engine = create_engine(url='sqlite:///app.db', connect_args={"check_same_thread": False})
        
        else:
            self._engine = create_engine(url=self.__db_url, pool_size=100, max_overflow=200, pool_timeout=1000)
        
        return self
    
    def __next__(self):
        if self._engine and self.__session == None:
            self.__session = sessionmaker(self._engine, expire_on_commit=False, class_=Session)
        
        if self.__session:
            return self.__session()
    
    
if __name__ == '__main__':
    from _all_models import AuthModel
    handler = iter(HandlerORM())
    next(handler)

    try:
        #db = handler.send('INIT')  # Primeira vez iniciando banco de dados
        #db = handler.send('SET')  # Banco de dados já iniciado

        
        with handler.send('set') as session:
            user = insert(AuthModel).values(name='name11', 
                                            passwd='senhateste11', 
                                            email='email11teste@app.com')
            session.execute(user)
            session.commit()
            session.close()
   
    except StopIteration:
        handler.close()
        #session.execute(text('CREATE TABLE user_name (id PRIMARY KEY NOT NULL , name TEXT)'))