from dataclasses import dataclass
from typing import Protocol

from app.application.gateway import FormPopulationReader, UserProvider
from app.application.interactor import Interactor
from app.domain.models import FormId, FormPopulation, OauthToken
from app.domain.services import FormPopulationService


class FormPopulationGateway(FormPopulationReader, Protocol): ...


@dataclass
class MatchFormIdDTO:
    form_id: FormId
    tocken: OauthToken


# TODO Refactor with smart DI
class MatchFormPopulations(Interactor[MatchFormIdDTO, list[FormPopulation]]):
    def __init__(
        self,
        form_population_db_gateway: FormPopulationGateway,
        form_population_service: FormPopulationService,
        user_provider: UserProvider,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service
        self.user_provider = user_provider

    async def __call__(self, data: MatchFormIdDTO) -> list[FormPopulation]:
        user = await self.user_provider.get_user(data.tocken)
        return await self.form_population_db_gateway.get_filtered_form_populations(
                user_email=user.email, form_id=data.form_id)
