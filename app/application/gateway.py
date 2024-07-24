from abc import abstractmethod
from typing import Protocol

from app.domain.models import FormId, FormPopulation, OauthTocken, User, UserEmail


class FormPopulationReader(Protocol):
    @abstractmethod
    def get_filtered_form_population(
        self, user_email: UserEmail, form_id: FormId
    ) -> FormPopulation:
        raise NotImplementedError

    @abstractmethod
    def get_filtered_form_populations_list(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        raise NotImplementedError


class FormPopulationSaver(Protocol):
    @abstractmethod
    def save_form_population(self, populations: FormPopulation) -> FormPopulation:
        raise NotImplementedError

    @abstractmethod
    def bulk_save_form_populations_list(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        raise NotImplementedError


class UserProvider(Protocol):
    @abstractmethod
    def get_user(self, oauth_tocken: OauthTocken) -> User:
        raise NotImplementedError
