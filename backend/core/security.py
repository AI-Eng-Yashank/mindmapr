from fastapi.requests import Request
from fastapi.security import HTTPBearer
from passlib.context import CryptContext

from core.config import settings

password_context = CryptContext(schemes=[ "bcrypt"], deprecated="auto")

reusable_oauth2 = HTTPBearer(scheme_name="Authorization")


def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_context.hash(password)


def is_unauthorized_url(request: Request):
    allow_urls = [
        "/",
    ]

    if not settings.IS_PRODUCTION:
        allow_urls.append("/docs")
        allow_urls.append("/openapi.json")

    current_url = request.url.path

    if current_url.startswith("/static"):
        return True

    if current_url in allow_urls:
        return True

    return False
