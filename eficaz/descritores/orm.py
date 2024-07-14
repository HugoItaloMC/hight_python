import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.engine import Engine


class Base(DeclarativeBase):
    ...


__engine: Engine = None

def create_engine():
    # Engine para gerar conexão com o banco de dados
    global __engine

    if __engine:
        return
    
    __engine = sa.create_engine(url="postgresql+psycopg2://auth:1cdc09ad55da@localhost:5433/auth")
    return __engine


def create_tables():
    # Iniciando banco de dados, lembrando que essa funcão é para testes pois a mesma 'zera' todos os dados
    global __engine

    if not __engine:
        create_engine()
    
    from __init__ import UserModel
    Base.metadata.drop_all(__engine)
    Base.metadata.create_all(__engine)


def create_session():
    # Gerando sessão com o banco de dados, assim poderemos enviar, deletar, editar dados na base de dados
    global __engine

    if not __engine:
        create_engine()
    __session = sessionmaker(bind=__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()
    return session
