from abc import ABC, abstractmethod
from typing import ContextManager

from app.application.create_form_populations_from_table import \
    CreateFormPopulationsFromTable
from app.application.create_user import CreateUser
from app.application.gateway import APIUserProvider, YandexUserProvider
from app.application.login_user import LoginUser
from app.application.match_form_population import MatchFormPopulations


class InteractorFactory(ABC):
    @abstractmethod
    def match_form_populations(
        self, user_provider: APIUserProvider
    ) -> ContextManager[MatchFormPopulations]:
        raise NotImplementedError

    @abstractmethod
    def create_form_populations_from_table(
        self, user_provider: APIUserProvider
    ) -> ContextManager[CreateFormPopulationsFromTable]:
        raise NotImplementedError

    @abstractmethod
    def login_user(
        self, yandex_id_provider: YandexUserProvider
    ) -> ContextManager[LoginUser]:
        raise NotImplementedError

    @abstractmethod
    def create_user(
        self, yandex_id_provider: YandexUserProvider
    ) -> ContextManager[CreateUser]:
        raise NotImplementedError
