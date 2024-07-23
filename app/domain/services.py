import typing

from .models import (
    FormPopulation,
    UnidentificatedFormPopulation,
    Parameter,
    UnidentificatedParameter,
    UserEmail,
    FormId,
)


_sentinel: typing.Any = object()


class FormPopulationService:
    @staticmethod
    def create(
        user_email: UserEmail, form_id: FormId, parameters: list[Parameter] = []
    ) -> FormPopulation:
        return UnidentificatedFormPopulation(
            user_email=user_email,
            form_id=form_id,
            parameters=parameters,
        )

    @staticmethod
    def add_parameter(form_population: FormPopulation, parameter: Parameter) -> None:
        form_population.parameters.append(parameter)


class ParameterService:
    @staticmethod
    def create(field: str, answer: str) -> Parameter:
        return UnidentificatedParameter(field=field, answer=answer)

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
