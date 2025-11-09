from fastapi import APIRouter
from app.config import db
from app.models import Skill

router = APIRouter()

@router.post("/skills")
async def add_skill(skill: Skill):
    await db["skills"].insert_one(skill.dict())
    return {"message": "Skill added"}

@router.get("/skills")
async def get_skills():
    skills = await db["skills"].find().to_list(100)
    return skills
