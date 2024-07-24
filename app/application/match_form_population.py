from dataclasses import dataclass
from typing import Protocol

from app.application.gateway import FormPopulationReader, UserProvider
from app.application.interactor import Interactor
from app.application.unit_of_work import UnitOfWork
from app.domain.models import FormId, FormPopulation, OauthTocken
from app.domain.services import FormPopulationService


class FormPopulationGateway(FormPopulationReader, Protocol): ...

@dataclass
class MatchFormIdDTO:
    form_id: FormId
    tocken: OauthTocken


# TODO Refactor with smart DI
class MatchFormPopulations(Interactor[MatchFormIdDTO, list[FormPopulation]]):
    def __init__(
        self,
        form_population_db_gateway: FormPopulationGateway,
        form_population_service: FormPopulationService,
        user_provider: UserProvider,
        uow: UnitOfWork,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service
        self.user_provider = user_provider
        self.uow = uow

    def __call__(
        self, data: MatchFormIdDTO) -> list[FormPopulation]:
        user = self.user_provider.get_user(data.tocken)
        populations = (
            self.form_population_db_gateway.get_filtered_form_populations_list(
                user_email=user.email, form_id=data.form_id
            )
        )
        return populations
