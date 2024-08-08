from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.domain.models import FormId, FormPopulation, User, UserEmail


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


class UserProvider(Protocol):
    """Interface for request dependency"""

    @abstractmethod
    async def get_user(self) -> User:
        raise NotImplementedError


class UserReader(Protocol):
    """Database interface"""

    @abstractmethod
    async def get_user(self, id: UUID, email: str) -> User:
        raise NotImplementedError


class UserSaver(Protocol):
    """Database interface"""

    @abstractmethod
    async def save_user(self, user: User) -> User:
        raise NotImplementedError
