from collections.abc import Iterator
from contextlib import contextmanager

from app.adapters.database.repository import FormPopulationGateway
from app.application.create_form_populations_from_table import (
    CreateFormPopulationsFromTable,
)
from app.application.gateway import UserProvider
from app.application.match_form_population import MatchFormPopulations
from app.domain.services import FormPopulationService
from app.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    def __init__(self) -> None:
        self.form_population_gateway = FormPopulationGateway()

    @contextmanager
    def match_form_populations( # type: ignore
        self, user_provider: UserProvider
    ) -> Iterator[MatchFormPopulations]:
        yield MatchFormPopulations(
            form_population_db_gateway=self.form_population_gateway,
            form_population_service=FormPopulationService(),
            user_provider=user_provider,
        )

    @contextmanager
    def create_form_populations_from_table( # type: ignore
        self,
    ) -> Iterator[CreateFormPopulationsFromTable]:
        yield CreateFormPopulationsFromTable( 
            form_population_db_gateway=self.form_population_gateway,
            form_population_service=FormPopulationService(),
        )
