from typing import NewType, Optional

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

ParameterId = NewType("ParameterId", str)
FormId = NewType("FormId", str)
FormPopulationId = NewType("FormPopulationId", str)
UserEmail = NewType("UserEmail", str)


@dataclass(config=ConfigDict(extra="ignore", from_attributes=True))
class User:
    email: UserEmail


@dataclass(config=ConfigDict(extra="ignore", from_attributes=True))
class Parameter:
    field: str
    answer: str
    id: Optional[ParameterId] = None


@dataclass(config=ConfigDict(extra="ignore", from_attributes=True))
class FormPopulation:
    user_email: UserEmail
    form_id: FormId
    parameters: list[Parameter]
    id: Optional[FormPopulationId] = None
