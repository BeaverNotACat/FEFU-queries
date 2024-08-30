from dataclasses import asdict
from typing import Any
from uuid import UUID

from app.adapters.database.connection import MongodbSessionManager
from app.adapters.database.models import FormPopulationODM, UserODM
from app.application.gateway import (
    FormPopulationReader,
    FormPopulationSaver,
    UserReader,
    UserSaver,
)
from app.domain.exceptions import AuthenticationError
from app.domain.models import FormId, FormPopulation, User, UserEmail

_sentinel: Any = object()


class FormPopulationGateway(FormPopulationReader, FormPopulationSaver):
    model = FormPopulationODM
    session_factory = MongodbSessionManager

    def __init__(self) -> None:
        self.session = self.session_factory()

    async def get_filtered_form_populations(
        self, user_email: UserEmail, form_id: FormId
    ) -> list[FormPopulation]:
        async with self.session:
            query = self.model.find(self.model.user_email == user_email).find(
                self.model.form_id == form_id
            )
            result = await query.to_list()
        return [FormPopulation(**population) for population in result]  # type: ignore

    async def bulk_save_form_populations(
        self, populations: list[FormPopulation]
    ) -> list[FormPopulation]:
        models = [FormPopulationODM(**asdict(population)) for population in populations]
        async with self.session:
            await self.model.insert_many(models)
        return populations  # TODO Get data from db


class UserDoesNotExist(AuthenticationError): ...


class UserGateway(UserReader, UserSaver):
    model = UserODM
    session_factory = MongodbSessionManager

    def __init__(self) -> None:
        self.session = self.session_factory()

    async def get_user(self, id: UUID = _sentinel, email: str = _sentinel) -> User:
        async with self.session:
            query = self.model.find()

            if id is not _sentinel:
                query = self.model.find(self.model.id == id)
            if email is not _sentinel:
                query = self.model.find(self.model.email == email)

            result = await query.first_or_none()
            if not result:
                raise UserDoesNotExist
            return User(**dict(result))

    async def save_user(self, user: User) -> User:
        data = asdict(user)
        if not user.id:
            del data["id"]

        model = self.model(**data)
        async with self.session:
            await self.model.insert(model)
        return await self.get_user(email=user.email)
