from csv import DictReader
from typing import Protocol

from litestar.datastructures import UploadFile

from app.application.gateway import FormPopulationSaver
from app.application.interactor import Interactor
from app.domain.models import FormPopulation
from app.domain.services import FormPopulationService


class FormPopulationGateway(FormPopulationSaver, Protocol): ...


NewFormPopulationsDTO = UploadFile


class CreateFormPopulationsFromTable(
    Interactor[NewFormPopulationsDTO, list[FormPopulation]]
):
    def __init__(
        self,
        form_population_db_gateway: FormPopulationGateway,
        form_population_service: FormPopulationService,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service

    async def __call__(self, data: NewFormPopulationsDTO) -> list[FormPopulation]:
        with open(data.file.seek(0)) as file:  # TODO Make it normal and such efficient
            translated_data = list(DictReader(file))
        populations = self.form_population_service.create_list(translated_data)
        await self.form_population_db_gateway.bulk_save_form_populations(populations)
        return populations
