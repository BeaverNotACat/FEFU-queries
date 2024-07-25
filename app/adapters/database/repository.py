from app.adapters.database.connection import mongodb_session_factory
from app.application.gateway import FormPopulationReader, FormPopulationSaver
from app.domain.models import UserEmail, FormId, FormPopulation
from app.adapters.database.models import FormPopulationODM

class FormPopulationGateway(FormPopulationReader, FormPopulationSaver):
    model = FormPopulationODM
    session_factory = mongodb_session_factory

    async def __init__(self) -> None:
        await self.session_factory()

    async def get_filtered_form_populations_list(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        query = FormPopulationODM.find(FormPopulationODM.user_email == user_email).find(FormPopulationODM.form_id == form_id)
        result = await query.to_list()
        return [FormPopulation(**population) for population in result] # type: ignore

    async def bulk_save_form_populations(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        raise NotImplementedError    
