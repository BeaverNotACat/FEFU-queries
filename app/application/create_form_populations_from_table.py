from typing import Protocol

from pandas import DataFrame

from app.application.gateway import FormPopulationSaver
from app.application.interactor import Interactor
from app.application.unit_of_work import UnitOfWork
from app.domain.models import FormPopulation
from app.domain.services import FormPopulationService


class FormPopulationGateway(FormPopulationSaver, Protocol): ...


NewFormPopulationsListDTO = DataFrame


class BulkCreateFormPopulation(
    Interactor[NewFormPopulationsListDTO, list[FormPopulation]]
):
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
        populations = self.form_population_service.bulk_create_from_table(data)
        self.form_population_db_gateway.bulk_save_form_populations_list(populations)
        self.uow.commit()
        return populations
