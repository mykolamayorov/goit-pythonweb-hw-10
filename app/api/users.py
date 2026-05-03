from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status, Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserResponse
from app.auth.deps import get_current_user
from app.models import User
from app.config import ME_RATE_LIMIT
from app.limiter import limiter
from app.services.cloudinary import upload_avatar

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
@limiter.limit(ME_RATE_LIMIT)
def me(request: Request, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/avatar", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_avatar(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if file.content_type not in ("image/jpeg", "image/png", "image/webp"):
        raise HTTPException(status_code=400, detail="Only JPEG/PNG/WEBP images are allowed")

    try:
        url = upload_avatar(file.file, public_id=f"user_{current_user.id}")
    except Exception:
        raise HTTPException(status_code=502, detail="Cloudinary upload failed")

    current_user.avatar_url = url
    db.commit()
    db.refresh(current_user)
    return current_user