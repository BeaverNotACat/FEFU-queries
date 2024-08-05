from .models import FormPopulation, Parameter, User

class ParameterService:
    @staticmethod
    def create(data: dict) -> Parameter:
        return Parameter(**data)

    @staticmethod
    def to_url_parameters(data: list[Parameter]) -> str:
        res = ""
        for item in data:
            res += f"&{item.field}={item.answer}"
        return res[1:]

    @staticmethod
    def create_from_dict(data: dict[str, str]) -> list[Parameter]:
        return [Parameter(field=field, answer=answer) for field, answer in data.items()]


# TODO refactor
class FormPopulationService:
    @staticmethod
    def create(data: dict) -> FormPopulation:
        return FormPopulation(**data)

    @staticmethod
    def create_list(data: list[dict]) -> list[FormPopulation]:
        return [FormPopulation(**row) for row in data]

    @staticmethod
    def add_parameter(form_population: FormPopulation, parameter: Parameter) -> None:
        form_population.parameters.append(parameter)

    @staticmethod
    def to_link_path(data: FormPopulation) -> str:
        return f"/{data.form_id}?{ParameterService.to_url_parameters(data.parameters)}"

class UserService:
    @staticmethod
    def create(data: dict) -> User:
        return User(**data)
