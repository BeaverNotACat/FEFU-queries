from beanie import Document


class Parameter(Document):
    field: str
    answer: str


class FormPopulation(Document):
    user_email: str
    form_id: str
    parameters: list[Parameter]
