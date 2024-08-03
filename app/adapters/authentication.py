import json

import httpx

from app.application.gateway import UserProvider
from app.domain.models import OauthToken, User
from app.domain.services import UserService


# TODO Refactor and make normal exception
class YandexIDAuth(UserProvider):
    URL = "https://login.yandex.ru/info"
    PARAMETERS = {"format": "json"}

    def __init__(self, oauth_token: OauthToken):
        self.token = oauth_token

    async def _send_request(self) -> dict:
        try:
            responce = httpx.get(
                url=self.URL,
                params=self.PARAMETERS,
                headers={"Authorization": self.token},
            )
            responce.raise_for_status()
            return json.loads(responce.json())
        except httpx.HTTPError as err:
            raise err

    async def get_user(self) -> User:
        return UserService.create(await self._send_request())
