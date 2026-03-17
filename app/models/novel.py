import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..core.database import Base
import enum


class NovelStatus(str, enum.Enum):
    ongoing = "ongoing"
    completed = "completed"
    hiatus = "hiatus"


class Novel(Base):
    __tablename__ = "novels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    synopsis = Column(Text, nullable=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    cover_url = Column(String, nullable=True)
    status = Column(Enum(NovelStatus), default=NovelStatus.ongoing, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    author = relationship("User", backref="novels")
    chapters = relationship("Chapter", back_populates="novel", cascade="all, delete-orphan")
