from datetime import date

from sqlalchemy import String, Date, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    first_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)

    birthday: Mapped[date] = mapped_column(Date, nullable=False)

    extra_data: Mapped[str | None] = mapped_column(Text, nullable=True)