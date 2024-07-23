from dataclasses import dataclass
from typing import NewType
from uuid import UUID


ParameterId = NewType("ParameterId", str)
FormId = NewType("FormId", str)
FormPopulationId = NewType("FormPopulationId", str)
UserEmail = NewType("UserEmail", str)


@dataclass
class User:
    email: UserEmail


@dataclass
class _BaseParameter:
    field: str
    answer: str

@dataclass
class UnidentificatedParameter(_BaseParameter):
    ...

@dataclass
class IdentificatedParameter(_BaseParameter):
    id: ParameterId

type Parameter = UnidentificatedParameter | IdentificatedParameter


@dataclass
class _BaseFormPopulation:
    user_email: UserEmail
    form_id: FormId
    parameters: list[Parameter]

@dataclass
class UnidentificatedFormPopulation(_BaseFormPopulation):
    ...

@dataclass
class IdentificatedFormPopulation(_BaseFormPopulation):
    id: FormPopulationId

type FormPopulation = UnidentificatedFormPopulation | IdentificatedFormPopulation
