import json

from app.application.gateway import UserProvider
from app.domain.models import OauthToken, User

import httpx

from app.domain.services import UserService

# TODO Refactor and make normal exception
class YandexIDAuth(UserProvider):
    URL = "https://login.yandex.ru/info"
    PARAMETERS = {"format": "json"}

    async def _send_request(self, oauth_tocken: OauthToken) -> dict:
        try:
            responce = httpx.get(
                url=self.URL,
                params=self.PARAMETERS,
                headers={"Authorization": oauth_tocken},
            )
            responce.raise_for_status()
            return json.loads(responce.json())
        except httpx.HTTPError as err:
            raise err

    async def get_user(self, oauth_tocken: OauthToken) -> User:
        return UserService.create(await self._send_request(oauth_tocken))
