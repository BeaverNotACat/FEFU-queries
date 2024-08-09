from csv import DictReader
from typing import Protocol

from litestar.datastructures import UploadFile

from app.application.gateway import FormPopulationSaver, UserProvider
from app.application.interactor import Interactor
from app.domain.exceptions import NoPermissionError
from app.domain.models import FormPopulation, UserRole
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
        user_provider: UserProvider,
    ) -> None:
        self.form_population_db_gateway = form_population_db_gateway
        self.form_population_service = form_population_service
        self.user_provider = user_provider

    async def __call__(self, data: NewFormPopulationsDTO) -> list[FormPopulation]:
        user = await self.user_provider.get_user()
        if user.role != UserRole.admin:
            raise NoPermissionError("Only admin can upload changes")

        with open(data.file.seek(0)) as file:  # TODO Make it normal and such efficient
            translated_data = list(DictReader(file))
        populations = self.form_population_service.create_list(translated_data)
        await self.form_population_db_gateway.bulk_save_form_populations(populations)
        return populations
