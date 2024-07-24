from dataclasses import dataclass
from typing import NewType, Optional

ParameterId = NewType("ParameterId", str)
FormId = NewType("FormId", str)
FormPopulationId = NewType("FormPopulationId", str)
UserEmail = NewType("UserEmail", str)


@dataclass
class User:
    email: UserEmail


@dataclass
class Parameter:
    field: str
    answer: str
    id: Optional[ParameterId] = None


@dataclass
class FormPopulation:
    user_email: UserEmail
    form_id: FormId
    parameters: list[Parameter]
    id: Optional[FormPopulationId] = None
