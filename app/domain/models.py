from enum import StrEnum
from typing import NewType, Optional

from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

ParameterId = NewType("ParameterId", str)
FormId = NewType("FormId", str)
FormPopulationId = NewType("FormPopulationId", str)
UserEmail = NewType("UserEmail", str)


class UserRole(StrEnum):
    user = "user"
    admin = "admin"


@dataclass(config=ConfigDict(extra="ignore", from_attributes=True))
class User:
    email: UserEmail
    role: UserRole


@dataclass(config=ConfigDict(extra="ignore", from_attributes=True))
class YandexUser:
    default_email: UserEmail


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
