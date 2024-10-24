from sqlalchemy import String, JSON
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Users(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    objects: Mapped[dict] = mapped_column(JSON)


