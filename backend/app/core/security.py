from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
import jwt
from typing import Annotated
from jwt.exceptions import InvalidTokenError
from ..schema import TokenData, UserInDB, User
from .db import fake_users_db
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


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


async def get_current_user(token: auth_depend):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentails",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt(token=token)
        username = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credential_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credential_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    return current_user


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
