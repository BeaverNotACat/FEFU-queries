from typing import Any

from litestar import Request
from litestar.connection import ASGIConnection
from litestar.security.jwt import JWTAuth, Token

from app.adapters.authentication import APIAuth
from app.settings import settings


async def retrieve_user_provider(
    token: Token, connection: ASGIConnection[Any, Any, Any, Any]
) -> APIAuth:
    return APIAuth(token)


api_auth: JWTAuth = JWTAuth(
    token_secret=settings.JWT_SECRET,
    retrieve_user_handler=retrieve_user_provider,
    exclude=["/schema", "/authenticate"],
)


async def api_auth_dependency(
    request: Request[APIAuth, Token, Any],
) -> APIAuth:
    return request.user
