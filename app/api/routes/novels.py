from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from ...core.database import get_db
from ...schemas.novel import NovelCreate, NovelUpdate, NovelResponse, NovelListResponse
from ...services import novel as novel_service
from ...models.novel import NovelStatus
from ...models.user import User, UserRole
from ..dependencies.auth import get_current_active_user, get_admin_user

router = APIRouter(prefix="/novels", tags=["Novels"])


def check_novel_owner_or_admin(novel, user: User):
    """Check if user is novel owner or admin."""
    if novel.author_id != user.id and user.role != UserRole.admin:
        return False
    return True


@router.get("", response_model=NovelListResponse)
def list_novels(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[NovelStatus] = None,
    db: Session = Depends(get_db)
):
    """List all novels with pagination."""
    return novel_service.get_novels(db, page, limit, status)


@router.get("/{novel_id}", response_model=NovelResponse)
def get_novel(novel_id: UUID, db: Session = Depends(get_db)):
    """Get a single novel by ID."""
    return novel_service.get_novel(db, novel_id)


@router.post("", response_model=NovelResponse, status_code=status.HTTP_201_CREATED)
def create_novel(
    novel_data: NovelCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new novel."""
    return novel_service.create_novel(db, novel_data, current_user.id)


@router.put("/{novel_id}", response_model=NovelResponse)
def update_novel(
    novel_id: UUID,
    novel_data: NovelUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a novel (owner or admin only)."""
    novel = novel_service.get_novel(db, novel_id)
    
    if not check_novel_owner_or_admin(novel, current_user):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this novel"
        )
    
    return novel_service.update_novel(db, novel_id, novel_data, current_user.id)


@router.delete("/{novel_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_novel(
    novel_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete a novel (owner or admin only)."""
    novel = novel_service.get_novel(db, novel_id)
    
    if not check_novel_owner_or_admin(novel, current_user):
        from fastapi import HTTPException
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this novel"
        )
    
    novel_service.delete_novel(db, novel_id)
    return None
