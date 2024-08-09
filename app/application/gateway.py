from abc import abstractmethod
from typing import Any, Protocol
from uuid import UUID

from app.domain.models import FormId, FormPopulation, User, UserEmail, YandexUser

_sentinel: Any = object()


class FormPopulationReader(Protocol):
    @abstractmethod
    async def get_filtered_form_populations(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        raise NotImplementedError


class FormPopulationSaver(Protocol):
    @abstractmethod
    async def bulk_save_form_populations(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        raise NotImplementedError


class YandexIDProvider(Protocol):
    """High level database interface"""

    @abstractmethod
    async def get_yandex_id(self) -> YandexUser:
        raise NotImplementedError


class UserProvider(Protocol):
    """High level database interface"""

    @abstractmethod
    async def get_user(self) -> User:
        raise NotImplementedError


class UserReader(Protocol):
    """Low level database interface for application layer gateways"""

    @abstractmethod
    async def get_user(self, id: UUID = _sentinel, email: str = _sentinel) -> User:
        raise NotImplementedError


class UserSaver(Protocol):
    """Low level database interface for application layer gateways"""

    @abstractmethod
    async def save_user(self, user: User) -> User:
        raise NotImplementedError
