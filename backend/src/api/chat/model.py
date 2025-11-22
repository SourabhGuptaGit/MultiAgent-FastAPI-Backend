from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, DateTime


def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)

class ChatMessagePayload(SQLModel):
    message: str

class ChatMessageListItems(SQLModel):
    id: int | None = Field(default=None)
    message: str
    created_at: datetime | None = Field(default=None)

class ChatMessage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False
    )