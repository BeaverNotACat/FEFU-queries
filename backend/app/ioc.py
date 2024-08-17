from collections.abc import Iterator
from contextlib import contextmanager

from app.adapters.database.repository import FormPopulationGateway, UserGateway
from app.application.create_form_populations_from_table import (
    CreateFormPopulationsFromTable,
)
from app.application.create_user import CreateUser
from app.application.gateway import UserProvider, YandexIDProvider
from app.application.login_user import LoginUser
from app.application.match_form_population import MatchFormPopulations
from app.domain.services import FormPopulationService, UserService
from app.presentation.interactor_factory import InteractorFactory


# TODO the fuck does mypy want
class IoC(InteractorFactory):
    def __init__(self) -> None:
        self.form_population_gateway = FormPopulationGateway()
        self.user_gateway = UserGateway()

    @contextmanager
    def match_form_populations(  # type: ignore
        self, user_provider: UserProvider
    ) -> Iterator[MatchFormPopulations]:
        yield MatchFormPopulations(
            form_population_db_gateway=self.form_population_gateway,
            form_population_service=FormPopulationService(),
            user_provider=user_provider,
        )

    @contextmanager
    def create_form_populations_from_table(  # type: ignore
        self, user_provider: UserProvider
    ) -> Iterator[CreateFormPopulationsFromTable]:
        yield CreateFormPopulationsFromTable(
            form_population_db_gateway=self.form_population_gateway,
            form_population_service=FormPopulationService(),
            user_provider=user_provider,
        )

    @contextmanager
    def login_user(self, yandex_id_provider: YandexIDProvider) -> Iterator[LoginUser]:
        yield LoginUser(
            user_db_gateway=self.user_gateway, yandex_id_provider=yandex_id_provider
        )

    @contextmanager
    def create_user(self, yandex_id_provider: YandexIDProvider) -> Iterator[CreateUser]:
        yield CreateUser(
            user_db_gateway=self.user_gateway,
            user_service=UserService(),
            yandex_id_provider=yandex_id_provider,
        )
