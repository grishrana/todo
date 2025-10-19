from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
import jwt
from typing import Annotated
from sqlmodel import select
from .db import Session_Dep
from ..models import Users
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_depend = Annotated[str, Depends(oauth2_scheme)]
password_hash = PasswordHash.recommended()


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)


def decode_jwt(token):
    return jwt.decode(token, settings.jwt_sec_key, algorithms=[settings.jwt_algo])


def authenticate_user(db, username: str, password: str):
    statement = select(Users).where(Users.username == username)
    user = db.exec(statement).first()
    if not user:
        return False
    if not verify_password(password, user.pw_hash):
        return False
    return user


async def get_current_user(token: auth_depend, session: Session_Dep):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentails",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_jwt(token=token)
    user_id = int(payload.get("sub"))  # subject is always string in JWT
    user = session.get(Users, user_id)
    if user is None:
        raise credential_exception
    return user


# Todo: Implement status on the User db
# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     if current_user.disabled:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
#         )grishrana7
#     return current_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.now(timezone.utc) + expires_delta
    else:
        expires = datetime.now(timezone.utc) + timedelta(
            minutes=settings.jwt_token_expire
        )
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_sec_key, algorithm=settings.jwt_algo
    )
    return encoded_jwt
