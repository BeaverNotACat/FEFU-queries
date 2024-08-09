from litestar import Controller, Response, get, post
from litestar.datastructures import UploadFile
from litestar.di import Provide

from app.adapters.authentication import Authentication, YandexIDAuth
from app.domain.exceptions import AuthenticationError
from app.domain.models import FormId, FormPopulation, User
from app.ioc import IoC
from app.presentation.authentication.jwt import jwt_auth, retrieve_user_provider
from app.presentation.authentication.yandexid import (
    yandex_id_dependency,
    yandex_id_middleware,
)
from app.presentation.dependencies import interactor_dependency


class ListFormPopulations(Controller):
    path = "/forms/{form_id: str}"
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "user_provider": Provide(retrieve_user_provider),
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
        "user_provider": Provide(retrieve_user_provider),
    }

    @post()
    async def list_form_populations(
        self, ioc: IoC, user_provider: Authentication, populations_table: UploadFile
    ) -> list[FormPopulation]:
        with ioc.create_form_populations_from_table(user_provider) as action:
            return await action(populations_table)


class Login(Controller):
    path = "/login"
    middleware = [yandex_id_middleware]
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "yandex_id_auth": Provide(yandex_id_dependency),
    }

    @post()
    async def login(self, ioc: IoC, yandex_id_auth: YandexIDAuth) -> Response[User]:
        try:
            with ioc.login_user(yandex_id_auth) as action:
                user = await action()
                return jwt_auth.login(identifier=str(user.id))
        except AuthenticationError:
            with ioc.create_user(yandex_id_auth) as action:
                user = await action()
                return jwt_auth.login(identifier=str(user.id))


class Register(Controller):
    path = "/register"
    middleware = [yandex_id_middleware]
    dependencies = {
        "ioc": Provide(interactor_dependency),
        "yandex_id_auth": Provide(yandex_id_dependency),
    }

    @post()
    async def register(self, ioc: IoC, yandex_id_auth: YandexIDAuth) -> Response[User]:
        with ioc.create_user(yandex_id_auth) as action:
            user = await action()
            return jwt_auth.login(identifier=str(user.id))
