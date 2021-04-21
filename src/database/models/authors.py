from __future__ import annotations
from datetime import date
from typing import Union

import sqlalchemy
from sqlalchemy.orm import Session, Query
from sqlalchemy_serializer import SerializerMixin

from src.database.db_session import SqlAlchemyBase


class Author(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'authors'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)

    birth_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    death_date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)

    @staticmethod
    def new(name: str, surname: str, birth_date: date, death_date: date) -> Author:
        author = Author()

        author.name = name
        author.surname = surname
        author.birth_date = birth_date
        author.death_date = death_date

        return author

    @staticmethod
    def _get_by(session: Session, params: dict[str, Union[str, date]], comparator, limit: int = 10) -> list[Author]:
        q: Query = session.query(Author).limit(limit)
        for attr, value in params.items():
            q = q.filter(comparator(getattr(Author, attr), value))
        return q.all()

    @staticmethod
    def get_like(session: Session, params: dict[str, Union[str, date]], limit: int = 10) -> list[Author]:
        return Author._get_by(
            session, params,
            lambda column, value: column.like("%%%s%%" % value), limit=limit,
        )

    @staticmethod
    def get_equal(session: Session, params: dict[str, Union[str, date]], limit: int = 10) -> list[Author]:
        return Author._get_by(
            session, params,
            lambda column, value: column._is(value), limit=limit,
        )
