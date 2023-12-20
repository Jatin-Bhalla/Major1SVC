from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets
#SECRET_KEY=secrets.token_hex(32)
SCERET_KEY = "151d9e98ad3748ae85d00e2535964619e33a7003da07c869214d312858995734"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
db = {
    "tim":{
        "username": "tim",
        "full_name": "Tim Ruscica",
        "email": "tim@gmail.com",
        "hashed_pass": "$2b$12$26QcftVZwe439mv7F18nMuBV/ZemWwN17OtZ0P4kS1ZSXD2.UDwOm", #hash from the name
        "disabled": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None

class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None

class UserInDB(User):
    hashed_pass: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()

@app.post()