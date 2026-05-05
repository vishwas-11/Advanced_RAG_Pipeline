from fastapi import APIRouter, HTTPException
from app.models.user import UserCreate, UserLogin
from app.services.auth import register_user, login_user

router = APIRouter()


@router.post("/register")
def register(data: UserCreate):
    user, error = register_user(data.name, data.email, data.password)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "message": "User created",
        "user_id": user["user_id"]
    }


@router.post("/login")
def login(data: UserLogin):
    token = login_user(data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }
