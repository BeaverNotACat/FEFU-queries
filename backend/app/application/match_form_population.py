from typing import Protocol

from app.application.gateway import FormPopulationReader, UserProvider
from app.application.interactor import Interactor
from app.domain.models import FormId, FormPopulation
from app.domain.services import FormPopulationService


class FormPopulationGateway(FormPopulationReader, Protocol): ...


class MatchFormPopulations(Interactor[FormId, list[FormPopulation]]):
    def __init__(
        self,
        form_population_db_gateway: FormPopulationGateway,
        form_population_service: FormPopulationService,
        user_provider: UserProvider,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service
        self.user_provider = user_provider

    async def __call__(self, form_id: FormId) -> list[FormPopulation]:
        user = await self.user_provider.get_user()
        return await self.form_population_db_gateway.get_filtered_form_populations(
            user_email=user.email, form_id=form_id
        )
