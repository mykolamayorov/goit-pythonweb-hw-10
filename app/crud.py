from datetime import date, timedelta

from sqlalchemy import and_, extract, or_
from sqlalchemy.orm import Session

from app.models import Contact
from app.schemas import ContactCreate, ContactUpdate


def create_contact(db: Session, contact_in: ContactCreate) -> Contact:
    contact = Contact(**contact_in.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def get_contacts(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
) -> list[Contact]:
    
    query = db.query(Contact)

    filters = []
    if first_name:
        filters.append(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        filters.append(Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        filters.append(Contact.email.ilike(f"%{email}%"))

    if filters:
        query = query.filter(and_(*filters))

    return query.offset(skip).limit(limit).all()


def get_contact_by_id(db: Session, contact_id: int) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


def get_contact_by_email(db: Session, email: str) -> Contact | None:
    return db.query(Contact).filter(Contact.email == email).first()


def update_contact(db: Session, contact: Contact, contact_in: ContactUpdate) -> Contact:
    data = contact_in.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(contact, key, value)

    db.commit()
    db.refresh(contact)
    return contact


def delete_contact(db: Session, contact: Contact) -> None:
    db.delete(contact)
    db.commit()


def get_upcoming_birthdays(db: Session, days: int = 7) -> list[Contact]:
    
    today = date.today()
    upcoming_days = [today + timedelta(days=i) for i in range(days)]

    conditions = [
        and_(
            extract("month", Contact.birthday) == d.month,
            extract("day", Contact.birthday) == d.day,
        )
        for d in upcoming_days
    ]

    return db.query(Contact).filter(or_(*conditions)).all()