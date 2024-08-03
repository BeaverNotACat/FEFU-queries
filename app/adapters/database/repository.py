from dataclasses import asdict

from app.adapters.database.connection import MongodbSessionManager
from app.adapters.database.models import FormPopulationODM
from app.application.gateway import FormPopulationReader, FormPopulationSaver
from app.domain.models import FormId, FormPopulation, UserEmail


class FormPopulationGateway(FormPopulationReader, FormPopulationSaver):
    model = FormPopulationODM
    session_factory = MongodbSessionManager

    def __init__(self) -> None:
        self.session = self.session_factory()

    async def get_filtered_form_populations(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        async with self.session:
            query = FormPopulationODM.find(
                FormPopulationODM.user_email == user_email
            ).find(FormPopulationODM.form_id == form_id)
            result = await query.to_list()
        return [FormPopulation(**population) for population in result]  # type: ignore

    async def bulk_save_form_populations(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        models = [FormPopulationODM(**asdict(population)) for population in populations]
        async with self.session:
            await FormPopulationODM.insert_many(models)
        return populations
