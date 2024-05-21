from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from database import db_settings


class DBHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )


db_helper = DBHelper(
    url=db_settings.url,
    echo=db_settings.echo,
)
