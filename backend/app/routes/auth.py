from fastapi import APIRouter, HTTPException
from app.config import db
from app.utils import hash_password, create_jwt, verify_password
from app.models import User

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    existing = await db["users"].find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    await db["users"].insert_one(user_dict)
    token = create_jwt({"email": user.email})
    return {"token": token, "user": {"email": user.email, "username": user.username}}

@router.post("/login")
async def login(user: User):
    existing = await db["users"].find_one({"email": user.email})
    if not existing or not verify_password(user.password, existing["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_jwt({"email": user.email})
    return {"token": token, "user": {"email": existing["email"], "username": existing["username"]}}
