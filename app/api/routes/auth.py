from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ...core.database import get_db
from ...schemas.user import UserCreate, UserResponse, UserLogin, Token
from ...services import auth as auth_service
from ..dependencies.auth import get_current_active_user
from ...models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    user = auth_service.register_user(db, user_data)
    return user


@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """Authenticate user and return access token."""
    user = auth_service.authenticate_user(db, login_data.email, login_data.password)
    return auth_service.create_user_token(user)


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Get current user information."""
    return current_user
