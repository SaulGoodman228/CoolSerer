from sqlalchemy import String, JSON, Integer
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    objects: Mapped[dict] = mapped_column(JSON)


