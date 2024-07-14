from datetime import datetime

from sqlalchemy import Integer, String, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.api.utils.base_model import Base


class Product(Base):
    __tablename__: str = 'product'

    id: Mapped[int] = mapped_column('id', BigInteger, autoincrement=True, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column('name', String(255), nullable=False, unique=True)
    size: Mapped[int] = mapped_column('size', Integer, nullable=False)
    date_create: Mapped[datetime] = mapped_column('date_create', DateTime, index=True, nullable=False, default=datetime.now)
