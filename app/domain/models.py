from dataclasses import dataclass
from typing import NewType
from uuid import UUID


ParameterId = NewType("ParameterId", UUID)
FormId = NewType("FormId", UUID)
FormPopulationId = NewType("FormPopulationId", UUID)
UserId = NewType("UserId", str)


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
    user_id: UserId
    form_id: FormId
    parameters: list[Parameter]

@dataclass
class UnidentificatedFormPopulation(_BaseFormPopulation):
    ...

@dataclass
class IdentificatedFormPopulation(_BaseFormPopulation):
    id: FormPopulationId

type FormPopulation = UnidentificatedFormPopulation | IdentificatedFormPopulation
