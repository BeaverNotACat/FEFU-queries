from dataclasses import dataclass
from typing import Protocol

from app.application.gateway import FormPopulationSaver
from app.application.interactor import Interactor
from app.application.unit_of_work import UnitOfWork
from app.domain.models import FormId, FormPopulation, Parameter, UserEmail
from app.domain.services import FormPopulationService


class FormPopulationGateway(
    FormPopulationSaver, Protocol
):
    ...

@dataclass
class NewFormPopulation:
    user_email: UserEmail
    parameters: list[Parameter]
     

@dataclass
class NewFormPopulationsListDTO:
    form_id: FormId
    populations: list[NewFormPopulation]
    
    

class BulkCreateFormPopulation(Interactor[FormPopulation, FormPopulation]):
    def __init__(
        self,
        form_population_db_gateway: FormPopulationGateway,
        form_population_service: FormPopulationService,
        uow: UnitOfWork,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service
        self.uow = uow

    def __call__(self, data: NewFormPopulationsListDTO) -> list[FormPopulation]:
        populations = [self.form_population_service.create(
            user_email=population.user_email,
            form_id=data.form_id,
            parameters=population.parameters,
            )
            for population in data.populations
        ]
        self.form_population_db_gateway.bulk_save_form_populations_list(populations)
        self.uow.commit()
        return populations        

