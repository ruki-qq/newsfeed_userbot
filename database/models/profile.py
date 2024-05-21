from datetime import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column

from database.enums import ProfileStatus
from database.models import Base


class Profile(Base):
    chat_id: Mapped[int] = mapped_column(BigInteger)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )
    status: Mapped[ProfileStatus] = mapped_column(
        default=ProfileStatus.ALIVE,
        server_default="ALIVE",
    )
    status_updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )

    def __str__(self):
        return f"{self.__class__.__name__}; id={self.id}; chat_id={self.chat_id}; status={self.status}"

    def __repr__(self):
        return f"'{str(self)}'"
