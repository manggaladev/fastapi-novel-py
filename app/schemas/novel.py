from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional, List
from ..models.novel import NovelStatus


class NovelCreate(BaseModel):
    title: str
    synopsis: Optional[str] = None
    cover_url: Optional[str] = None
    status: Optional[NovelStatus] = NovelStatus.ongoing


class NovelUpdate(BaseModel):
    title: Optional[str] = None
    synopsis: Optional[str] = None
    cover_url: Optional[str] = None
    status: Optional[NovelStatus] = None


class NovelResponse(BaseModel):
    id: UUID
    title: str
    synopsis: Optional[str]
    cover_url: Optional[str]
    status: NovelStatus
    author_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NovelListResponse(BaseModel):
    items: List[NovelResponse]
    total: int
    page: int
    limit: int
    total_pages: int
