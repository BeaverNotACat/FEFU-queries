from abc import abstractmethod
from typing import Protocol

from app.domain.models import FormId, FormPopulation, OauthToken, User, UserEmail


class FormPopulationReader(Protocol):
    @abstractmethod
    async def get_one_form_population(
        self, user_email: UserEmail, form_id: FormId
    ) -> FormPopulation:
        raise NotImplementedError

    @abstractmethod
    async def get_filtered_form_populations(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        raise NotImplementedError


class FormPopulationSaver(Protocol):
    @abstractmethod
    async def save_form_population(self, populations: FormPopulation) -> FormPopulation:
        raise NotImplementedError

    @abstractmethod
    async def bulk_save_form_populations(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        raise NotImplementedError


class UserProvider(Protocol):
    @abstractmethod
    async def get_user(self, oauth_tocken: OauthToken) -> User:
        raise NotImplementedError
