from beanie import Document


class ParameterODM(Document):
    field: str
    answer: str


class FormPopulationODM(Document):
    user_email: str
    form_id: str
    parameters: list[ParameterODM]
