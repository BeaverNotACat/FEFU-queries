from litestar.connection import ASGIConnection, Request
from litestar.datastructures.state import State
from litestar.exceptions import NotAuthorizedException
from litestar.middleware import (
    AbstractAuthenticationMiddleware,
    AuthenticationResult,
    DefineMiddleware,
)

from app.adapters.authentication import AuthenticationError, YandexIDAuth

API_KEY_HEADER = "Authorization"


class AuthenticationMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(
        self, connection: ASGIConnection
    ) -> AuthenticationResult:
        auth_header = connection.headers.get(API_KEY_HEADER)
        if not auth_header:
            raise NotAuthorizedException()
        try:
            await YandexIDAuth(auth_header).get_user()
        except AuthenticationError:
            raise NotAuthorizedException("Your token is mailformed")

        return AuthenticationResult(user=YandexIDAuth(auth_header), auth=None)


auth_mw = DefineMiddleware(AuthenticationMiddleware)


async def user_manager_dependency(
    request: Request[YandexIDAuth, None, State],
) -> YandexIDAuth:
    return request.user
