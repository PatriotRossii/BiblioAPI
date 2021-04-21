from datetime import date
from typing import Union

from sqlalchemy.orm import Query, Session

from src.database.db_session import SqlAlchemyBase


class ModelBase(SqlAlchemyBase):
    @classmethod
    def _get_by(cls, session: Session, params: dict[str, Union[str, date]], comparator, limit: int = 10):
        q: Query = session.query(cls.__name__).limit(limit)
        for attr, value in params.items():
            q = q.filter(comparator(getattr(cls.__name__, attr), value))
        return q.all()

    @classmethod
    def get_like(cls, session: Session, params: dict[str, Union[str, date]], limit: int = 10):
        return cls.__name__._get_by(
            session, params,
            lambda column, value: column.like("%%%s%%" % value), limit=limit,
        )

    @classmethod
    def get_equal(cls, session: Session, params: dict[str, Union[str, date]], limit: int = 10):
        return cls.__name__._get_by(
            session, params,
            lambda column, value: column._is(value), limit=limit,
        )
