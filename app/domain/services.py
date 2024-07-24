import typing

from pandas import DataFrame

from app.domain.exceptions import WrongTableFormat

from .models import FormId, FormPopulation, Parameter, UserEmail

_sentinel: typing.Any = object()


class FormPopulationService:
    def _try_to_map_dict(self, data: dict):
        try:
            user_email = data["user_email"]
            del data[user_email]
            form_id = data["form_id"]
            del data[form_id]
            return FormPopulation(
                user_email=data["user_email"],
                form_id=data["form_id"],
                parameters=ParameterService.create_list_from_dict(data),
            )
        except KeyError:
            raise WrongTableFormat

    def create(
        self, user_email: UserEmail, form_id: FormId, parameters: list[Parameter] = []
    ) -> FormPopulation:
        return FormPopulation(
            user_email=user_email,
            form_id=form_id,
            parameters=parameters,
        )

    def bulk_create_from_table(self, data: DataFrame) -> list[FormPopulation]:
        populations = []
        for row in data.to_dict("records"):
            populations.append(self._try_to_map_dict(row))
        return populations

    @staticmethod
    def add_parameter(form_population: FormPopulation, parameter: Parameter) -> None:
        form_population.parameters.append(parameter)


class ParameterService:
    @staticmethod
    def create(field: str, answer: str) -> Parameter:
        return Parameter(field=field, answer=answer)

    @staticmethod
    def create_list_from_dict(data: dict[str, str]) -> list[Parameter]:
        return [Parameter(field=field, answer=answer) for field, answer in data.items()]

    @staticmethod
    def update(
        parameter: Parameter,
        new_field: str = _sentinel,
        new_answer: str = _sentinel,
    ) -> None:
        if new_field is not _sentinel:
            parameter.field = new_field

        if new_answer is not _sentinel:
            parameter.answer = new_answer
