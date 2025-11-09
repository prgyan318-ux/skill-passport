from pydantic import BaseModel

# For authentication
class User(BaseModel):
    username: str
    email: str
    password: str

# Skills
class Skill(BaseModel):
    name: str
    level: str
