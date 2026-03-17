from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from uuid import UUID
from fastapi import HTTPException, status
from ..models.novel import Novel, NovelStatus
from ..schemas.novel import NovelCreate, NovelUpdate, NovelListResponse, NovelResponse


def create_novel(db: Session, novel_data: NovelCreate, author_id: UUID) -> Novel:
    db_novel = Novel(
        title=novel_data.title,
        synopsis=novel_data.synopsis,
        cover_url=novel_data.cover_url,
        status=novel_data.status or NovelStatus.ongoing,
        author_id=author_id
    )
    db.add(db_novel)
    db.commit()
    db.refresh(db_novel)
    return db_novel


def get_novel(db: Session, novel_id: UUID) -> Novel:
    novel = db.query(Novel).filter(Novel.id == novel_id).first()
    if not novel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Novel not found"
        )
    return novel


def get_novels(
    db: Session,
    page: int = 1,
    limit: int = 10,
    status: Optional[NovelStatus] = None
) -> NovelListResponse:
    query = db.query(Novel)
    
    if status:
        query = query.filter(Novel.status == status)
    
    total = query.count()
    total_pages = (total + limit - 1) // limit
    
    novels = query.order_by(Novel.created_at.desc()).offset((page - 1) * limit).limit(limit).all()
    
    return NovelListResponse(
        items=[NovelResponse.model_validate(novel) for novel in novels],
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages
    )


def update_novel(db: Session, novel_id: UUID, novel_data: NovelUpdate, user_id: UUID) -> Novel:
    novel = get_novel(db, novel_id)
    
    update_data = novel_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(novel, key, value)
    
    db.commit()
    db.refresh(novel)
    return novel


def delete_novel(db: Session, novel_id: UUID) -> None:
    novel = get_novel(db, novel_id)
    db.delete(novel)
    db.commit()
