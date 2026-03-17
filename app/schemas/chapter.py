from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional, List


class ChapterCreate(BaseModel):
    title: str
    chapter_number: int
    content: str


class ChapterUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class ChapterResponse(BaseModel):
    id: UUID
    title: str
    chapter_number: int
    novel_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ChapterDetailResponse(BaseModel):
    id: UUID
    title: str
    chapter_number: int
    content: str
    novel_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ChapterListResponse(BaseModel):
    items: List[ChapterResponse]
    total: int
    page: int
    limit: int
    total_pages: int
