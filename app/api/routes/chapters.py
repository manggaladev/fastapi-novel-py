from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from ...core.database import get_db
from ...schemas.chapter import ChapterCreate, ChapterUpdate, ChapterResponse, ChapterDetailResponse, ChapterListResponse
from ...services import chapter as chapter_service
from ...services import novel as novel_service
from ...models.user import User, UserRole
from ..dependencies.auth import get_current_active_user

router = APIRouter(tags=["Chapters"])


def check_novel_owner_or_admin(novel, user: User):
    """Check if user is novel owner or admin."""
    if novel.author_id != user.id and user.role != UserRole.admin:
        return False
    return True


def check_chapter_owner_or_admin(chapter, user: User, db: Session):
    """Check if user is chapter's novel owner or admin."""
    novel = novel_service.get_novel(db, chapter.novel_id)
    return check_novel_owner_or_admin(novel, user)


@router.get("/novels/{novel_id}/chapters", response_model=ChapterListResponse)
def list_chapters(
    novel_id: UUID,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """List all chapters for a novel with pagination."""
    # Verify novel exists
    novel_service.get_novel(db, novel_id)
    return chapter_service.get_chapters_by_novel(db, novel_id, page, limit)


@router.get("/chapters/{chapter_id}", response_model=ChapterDetailResponse)
def get_chapter(chapter_id: UUID, db: Session = Depends(get_db)):
    """Get a single chapter with content."""
    return chapter_service.get_chapter(db, chapter_id)


@router.post("/novels/{novel_id}/chapters", response_model=ChapterResponse, status_code=status.HTTP_201_CREATED)
def create_chapter(
    novel_id: UUID,
    chapter_data: ChapterCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new chapter (novel owner or admin only)."""
    novel = novel_service.get_novel(db, novel_id)
    
    if not check_novel_owner_or_admin(novel, current_user):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create chapters for this novel"
        )
    
    return chapter_service.create_chapter(db, novel_id, chapter_data)


@router.put("/chapters/{chapter_id}", response_model=ChapterResponse)
def update_chapter(
    chapter_id: UUID,
    chapter_data: ChapterUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a chapter (novel owner or admin only)."""
    chapter = chapter_service.get_chapter(db, chapter_id)
    
    if not check_chapter_owner_or_admin(chapter, current_user, db):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this chapter"
        )
    
    return chapter_service.update_chapter(db, chapter_id, chapter_data)


@router.delete("/chapters/{chapter_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chapter(
    chapter_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete a chapter (novel owner or admin only)."""
    chapter = chapter_service.get_chapter(db, chapter_id)
    
    if not check_chapter_owner_or_admin(chapter, current_user, db):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this chapter"
        )
    
    chapter_service.delete_chapter(db, chapter_id)
    return None
