from pydantic import BaseModel, EmailStr
from typing import Optional  # 👈 Agregado para compatibilidad con Python 3.9

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str  
    class Config:
        from_attributes = True  # En Pydantic v2 reemplaza a orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None  # 👈 Modificado para Python 3.9
# RECUPERACION DE CONTRASE˜NA
class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
