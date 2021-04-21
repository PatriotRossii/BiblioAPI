from __future__ import annotations
from datetime import date
from typing import Union

import sqlalchemy
from sqlalchemy.orm import Session, Query
from sqlalchemy_serializer import SerializerMixin

from src.database.db_session import SqlAlchemyBase
from src.database.models.ModelBase import ModelBase


class Author(ModelBase, SerializerMixin):
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
