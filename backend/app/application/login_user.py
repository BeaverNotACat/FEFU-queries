from typing import Protocol

from app.application.gateway import UserReader, YandexUserProvider
from app.application.interactor import Interactor
from app.domain.models import User


class UserGateway(UserReader, Protocol): ...


class LoginUser(Interactor[None, User]):
    def __init__(
        self,
        user_db_gateway: UserGateway,
        yandex_id_provider: YandexUserProvider,
    ) -> None:
        self.user_db_gateway = user_db_gateway
        self.yandex_id_provider = yandex_id_provider

    async def __call__(self, data=None) -> User:
        yandex_user = await self.yandex_id_provider.get_user()
        email = yandex_user.default_email
        return await self.user_db_gateway.get_user(email=email)
