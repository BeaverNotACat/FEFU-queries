from litestar import Controller, get, post
from litestar.datastructures import UploadFile
from litestar.di import Provide

from app.adapters.authentication import Authentication
from app.domain.models import FormId, FormPopulation
from app.ioc import IoC
from app.presentation.dependencies import interactor_dependency


class ListFormPopulations(Controller):
    path = "/forms/{form_id: str}"
    dependencies = {
        "ioc": Provide(interactor_dependency),
    }

    @get()
    async def list_form_populations(
        self, ioc: IoC, user_provider: Authentication, form_id: FormId
    ) -> list[FormPopulation]:
        with ioc.match_form_populations(user_provider) as action:
            return await action(form_id)


class CreateFormPopulations(Controller):
    path = "/forms"
    dependencies = {
        "ioc": Provide(interactor_dependency),
    }

    @post()
    async def list_form_populations(
        self, ioc: IoC, populations_table: UploadFile
    ) -> list[FormPopulation]:
        with ioc.create_form_populations_from_table() as action:
            return await action(populations_table)
