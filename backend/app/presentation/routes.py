from litestar import Controller, Response, get, post
from litestar.datastructures import UploadFile
from litestar.di import Provide
from litestar.security.jwt import Token

from app.adapters.authentication import Authentication, YandexIDAuth
from app.domain.exceptions import AuthenticationError
from app.domain.models import FormId, FormPopulation, User
from app.ioc import IoC
from app.presentation.authentication.jwt import jwt_auth, user_dependency
from app.presentation.authentication.yandexid import (
    yandex_id_dependency,
    yandex_id_middleware,
)
from app.presentation.dependencies import interactor_dependency


class ListFormPopulations(Controller):
    path = "/forms/{form_id: str}"
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "auth": Provide(user_dependency),
    }

    @get()
    async def list_form_populations(
        self, ioc: IoC, auth: Authentication, form_id: FormId
    ) -> list[FormPopulation]:
        with ioc.match_form_populations(auth) as action:
            return await action(form_id)


class CreateFormPopulations(Controller):
    path = "/forms"
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "auth": Provide(user_dependency),
    }

    @post()
    async def create_form_populations(
        self, ioc: IoC, auth: Authentication, populations_table: UploadFile
    ) -> list[FormPopulation]:
        with ioc.create_form_populations_from_table(auth) as action:
            return await action(populations_table)


class Authentication(Controller):
    path = "/authenticate"
    middleware = [yandex_id_middleware]
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "yandex_id_auth": Provide(yandex_id_dependency),
    }

    @post()
    async def authenticate(self, ioc: IoC, yandex_id_auth: YandexIDAuth) -> Response[User]:
        try:
            with ioc.login_user(yandex_id_auth) as action:
                user = await action()
        except AuthenticationError:
            with ioc.create_user(yandex_id_auth) as action:
                user = await action()
        return jwt_auth.login(identifier=str(user.id), response_body=user)
