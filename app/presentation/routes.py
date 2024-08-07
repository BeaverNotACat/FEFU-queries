from litestar import Controller, get
from litestar.di import Provide
from litestar.response import Template

from app.adapters.authentication import YandexIDAuth
from app.domain.models import FormId, FormPopulation
from app.ioc import IoC
from app.presentation.authentication import user_provider_dependency
from app.presentation.dependencies import interactor_dependency


class ListFormPopulations(Controller):
    path = "/forms/{form_id: str}"
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "user_provider": Provide(user_provider_dependency),
    }

    @get()
    async def list_form_populations(
        self, ioc: IoC, user_provider: YandexIDAuth, form_id: FormId
    ) -> list[FormPopulation]:
        with ioc.match_form_populations(user_provider) as action:
            return await action(form_id)
