from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field

from app.domain.models import UserRole


class ParameterODM(Document):
    field: str
    answer: str


class FormPopulationODM(Document):
    user_email: str
    form_id: str
    parameters: list[ParameterODM]


class UserODM(Document):
    id: UUID = Field(default_factory=uuid4)  # type: ignore
    email: str
    role: UserRole
