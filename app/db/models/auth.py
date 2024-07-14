from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, BigInteger, DateTime

from app.utils.base_model import Base


class User(Base):
    __tablename__: str = 'user'

    id: Mapped[int] = mapped_column('id', BigInteger, autoincrement=True, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column('name', String(255), nullable=False, unique=True)
    passwd: Mapped[str] = mapped_column('passwd', String(255), nullable=False)
    email: Mapped[str] = mapped_column('email', String(140), unique=True, nullable=False)
    date_create: Mapped[datetime] = mapped_column('date_create', DateTime, index=True, nullable=False, default=datetime.now)
