from typing import Protocol

from app.application.gateway import UserSaver, YandexIDProvider
from app.application.interactor import Interactor
from app.domain.models import User, UserRole
from app.domain.services import UserService


class UserGateway(UserSaver, Protocol): ...


class CreateUser(Interactor[None, User]):
    def __init__(
        self,
        user_db_gateway: UserGateway,
        user_service: UserService,
        yandex_id_provider: YandexIDProvider,
    ) -> None:
        self.user_db_gateway = user_db_gateway
        self.user_service = user_service
        self.yandex_id_provider = yandex_id_provider

    async def __call__(self, data=None) -> User:
        yandex_user = await self.yandex_id_provider.get_yandex_id()
        data = {
            "email": yandex_user.default_email,
            "role": UserRole.user,
        }
        user = self.user_service.create(data)
        return await self.user_db_gateway.save_user(user)
