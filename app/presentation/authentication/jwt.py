from typing import Any

from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTAuth, Token

from app.adapters.authentication import Authentication
from app.settings import settings


async def retrieve_user_provider(
    token: Token, connection: ASGIConnection[Any, Any, Any, Any]
) -> Authentication:
    return Authentication(token)


jwt_auth: JWTAuth = JWTAuth(
    token_secret=settings.JWT_SECRET, retrieve_user_handler=retrieve_user_provider
)
