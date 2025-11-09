from fastapi import FastAPI
from app.routes import auth, skills

app = FastAPI(title="Skill Passport Backend")

app.include_router(auth.router, prefix="/auth")
app.include_router(skills.router)
