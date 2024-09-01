from uuid import UUID

import httpx
from litestar.security.jwt import Token

from app.adapters.database.repository import UserGateway
from app.application.gateway import APIUserProvider, YandexUserProvider
from app.domain.exceptions import AuthenticationError
from app.domain.models import User, YandexUser


class YandexIDAuth(YandexUserProvider):
    URL = "https://login.yandex.ru/info"
    PARAMETERS = {"format": "json"}

    def __init__(self, oauth_token: str):
        self.token = oauth_token

    async def _autenthicate(self) -> dict:
        try:
            responce = httpx.get(
                url=self.URL,
                params=self.PARAMETERS,
                headers={"Authorization": self.token},
            )
            responce.raise_for_status()
            return responce.json()
        except httpx.HTTPStatusError:
            raise AuthenticationError("Unable to authorize with Yandex ID")

    async def get_user(self) -> YandexUser:
        user = await self._autenthicate()
        return YandexUser(**user)


class APIAuth(APIUserProvider):
    def __init__(self, token: Token):
        self.token = token

    async def get_user(self) -> User:
        return await UserGateway().get_user(id=UUID(Token.sub))
