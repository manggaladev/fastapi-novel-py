from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID
from fastapi import HTTPException, status
from ..models.chapter import Chapter
from ..schemas.chapter import ChapterCreate, ChapterUpdate, ChapterListResponse, ChapterResponse, ChapterDetailResponse


def create_chapter(db: Session, novel_id: UUID, chapter_data: ChapterCreate) -> Chapter:
    # Check if chapter number already exists for this novel
    existing = db.query(Chapter).filter(
        Chapter.novel_id == novel_id,
        Chapter.chapter_number == chapter_data.chapter_number
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Chapter number already exists for this novel"
        )
    
    db_chapter = Chapter(
        title=chapter_data.title,
        chapter_number=chapter_data.chapter_number,
        content=chapter_data.content,
        novel_id=novel_id
    )
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


def get_chapter(db: Session, chapter_id: UUID) -> Chapter:
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chapter not found"
        )
    return chapter


def get_chapters_by_novel(
    db: Session,
    novel_id: UUID,
    page: int = 1,
    limit: int = 10
) -> ChapterListResponse:
    query = db.query(Chapter).filter(Chapter.novel_id == novel_id)
    
    total = query.count()
    total_pages = (total + limit - 1) // limit
    
    chapters = query.order_by(Chapter.chapter_number.asc()).offset((page - 1) * limit).limit(limit).all()
    
    return ChapterListResponse(
        items=[ChapterResponse.model_validate(chapter) for chapter in chapters],
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )


def update_chapter(db: Session, chapter_id: UUID, chapter_data: ChapterUpdate) -> Chapter:
    chapter = get_chapter(db, chapter_id)
    
    update_data = chapter_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(chapter, key, value)
    
    db.commit()
    db.refresh(chapter)
    return chapter


def delete_chapter(db: Session, chapter_id: UUID) -> None:
    chapter = get_chapter(db, chapter_id)
    db.delete(chapter)
    db.commit()
